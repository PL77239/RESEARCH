"""Generate assets/poland-cee-map.svg from Natural Earth 1:50m country borders.

Usage:
    curl -sL -o /tmp/ne50.geojson \
      https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson
    python3 tools/make_map.py /tmp/ne50.geojson assets/poland-cee-map.svg
"""

import json
import math
import sys

LON_MIN, LON_MAX = 8.5, 30.5
LAT_MIN, LAT_MAX = 46.0, 57.5
REF_LAT = 52.0
WIDTH = 1000

NEIGHBOURS = {"DEU", "CZE", "SVK", "UKR", "BLR", "LTU", "LVA", "RUS", "HUN", "AUT", "ROU", "DNK", "SWE", "MDA", "EST"}

CITIES = [
    ("Warsaw", 21.01, 52.23),
    ("Kraków", 19.94, 50.06),
    ("Gdańsk", 18.65, 54.35),
    ("Poznań", 16.93, 52.41),
    ("Wrocław", 17.03, 51.11),
]

kx = math.cos(math.radians(REF_LAT))
scale = WIDTH / ((LON_MAX - LON_MIN) * kx)
HEIGHT = round((LAT_MAX - LAT_MIN) * scale)


def project(lon, lat):
    return (lon - LON_MIN) * kx * scale, (LAT_MAX - lat) * scale


def polygons(geom):
    return geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]


def in_view(poly):
    return any(LON_MIN - 3 < lon < LON_MAX + 3 and LAT_MIN - 3 < lat < LAT_MAX + 3 for lon, lat in poly[0])


def to_path(geom):
    parts = []
    for poly in polygons(geom):
        if not in_view(poly):
            continue
        for ring in poly:
            pts = [project(lon, lat) for lon, lat in ring]
            parts.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + "Z")
    return "".join(parts)


def main(src, dst):
    data = json.load(open(src))
    poland, others = "", []
    for f in data["features"]:
        code = f["properties"]["ADM0_A3"]
        if code == "POL":
            poland = to_path(f["geometry"])
        elif code in NEIGHBOURS:
            path = to_path(f["geometry"])
            if path:
                others.append(path)

    cities = []
    for name, lon, lat in CITIES:
        x, y = project(lon, lat)
        cities.append(f'<circle class="city" data-name="{name}" cx="{x:.1f}" cy="{y:.1f}" r="7"/>')

    _, poland_top = project(0, 54.9)
    _, poland_bottom = project(0, 49.0)
    flag_split = (project(0, 52.0)[1] - poland_top) / (poland_bottom - poland_top)
    style = (
        "<defs>"
        f'<linearGradient id="flag" gradientUnits="userSpaceOnUse" x1="0" y1="{poland_top:.0f}" x2="0" y2="{poland_bottom:.0f}">'
        f'<stop offset="{flag_split:.3f}" stop-color="#ffffff"/><stop offset="{flag_split:.3f}" stop-color="#dc143c"/>'
        "</linearGradient></defs>"
        "<style>"
        ".neighbours path{fill:rgba(255,255,255,.05);stroke:rgba(255,255,255,.28);stroke-width:1.6;stroke-linejoin:round}"
        ".poland{fill:url(#flag);stroke:#ffffff;stroke-width:3;stroke-linejoin:round}"
        ".city{fill:#f39200;stroke:#081f45;stroke-width:3}"
        "</style>"
    )
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}">{style}'
        f'<g class="neighbours">{"".join(f"<path d=\"{p}\"/>" for p in others)}</g>'
        f'<path class="poland" d="{poland}"/>'
        f'<g class="cities">{"".join(cities)}</g>'
        "</svg>"
    )
    open(dst, "w").write(svg)
    print(f"wrote {dst} ({WIDTH}x{HEIGHT})")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
