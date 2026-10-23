"""Draws the Type 1 vs Type 2 hypervisor architecture diagram (EN and PL)."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

LABELS = {
    "en": {
        "t1": "Type 1 (bare-metal / native)",
        "t2": "Type 2 (hosted)",
        "app": "Apps",
        "gos": "Guest OS",
        "vm": "VM",
        "hv": "Hypervisor (VMM)",
        "hos": "Host operating system",
        "hw": "Physical hardware (CPU with VT-x / AMD-V, RAM, disks, NIC)",
        "hv2": "Hypervisor (application)",
        "happ": "Other host apps",
    },
    "pl": {
        "t1": "Typ 1 (bare-metal / natywny)",
        "t2": "Typ 2 (hostowany)",
        "app": "Aplikacje",
        "gos": "System gościa",
        "vm": "VM",
        "hv": "Hypervisor (VMM)",
        "hos": "System operacyjny hosta",
        "hw": "Sprzęt fizyczny (CPU z VT-x / AMD-V, RAM, dyski, karta sieciowa)",
        "hv2": "Hypervisor (aplikacja)",
        "happ": "Inne aplikacje hosta",
    },
}

C_HW = "#5b6770"
C_HV = "#1f6fb2"
C_OS = "#7a9a3a"
C_VM = "#e8eef5"
C_GOS = "#f2a541"
C_APP = "#f7d488"


def box(ax, x, y, w, h, color, text, fc_text="white", size=9, bold=False):
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.005,rounding_size=0.08",
            linewidth=1, edgecolor="#333333", facecolor=color,
        )
    )
    ax.text(
        x + w / 2, y + h / 2, text, ha="center", va="center",
        fontsize=size, color=fc_text, wrap=True,
        fontweight="bold" if bold else "normal",
    )


def vm_stack(ax, x, y, w, t):
    box(ax, x, y, w, 2.15, C_VM, "", size=8)
    ax.text(x + 0.08, y + 2.0, t["vm"], fontsize=7, color="#333333", va="top")
    box(ax, x + 0.1, y + 0.1, w - 0.2, 0.75, C_GOS, t["gos"], fc_text="black", size=8)
    box(ax, x + 0.1, y + 0.95, w - 0.2, 0.75, C_APP, t["app"], fc_text="black", size=8)


def panel_type1(ax, t):
    ax.set_title(t["t1"], fontsize=11, fontweight="bold")
    box(ax, 0, 0, 6, 0.9, C_HW, t["hw"], size=8)
    box(ax, 0, 1.0, 6, 0.9, C_HV, t["hv"], bold=True)
    for i in range(3):
        vm_stack(ax, 0.05 + i * 2.0, 2.0, 1.9, t)


def panel_type2(ax, t):
    ax.set_title(t["t2"], fontsize=11, fontweight="bold")
    box(ax, 0, 0, 6, 0.9, C_HW, t["hw"], size=8)
    box(ax, 0, 1.0, 6, 0.9, C_OS, t["hos"], bold=True)
    box(ax, 0, 2.0, 4.0, 0.7, C_HV, t["hv2"], size=9, bold=True)
    box(ax, 4.1, 2.0, 1.9, 2.95, "#c9d6b0", t["happ"], fc_text="black", size=8)
    vm_stack(ax, 0.05, 2.8, 1.9, t)
    vm_stack(ax, 2.05, 2.8, 1.9, t)


def draw(lang: str, path: str) -> None:
    t = LABELS[lang]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.4))
    for ax in axes:
        ax.set_xlim(-0.1, 6.1)
        ax.set_ylim(-0.1, 5.1)
        ax.axis("off")
    panel_type1(axes[0], t)
    panel_type2(axes[1], t)
    fig.tight_layout()
    fig.savefig(path, dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    import sys

    draw(sys.argv[1], sys.argv[2])
