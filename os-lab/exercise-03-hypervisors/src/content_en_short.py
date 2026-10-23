TITLE_PAGE = {
    "compact": True,
    "line_spacing": 1.15,
    "course": "Operating Systems",
    "exercise": "Exercise 3",
    "title": "Type 1 vs Type 2 hypervisors and server-designed virtualisers",
    "fields": [
        ("Name", "[[First name Last name]]"),
        ("Student ID", "[[000000]]"),
        ("Group", "[[Group]]"),
        ("Date", "[[date]]"),
    ],
}

BODY = [
    ("h2", "1. Definitions"),
    ("p",
     "A **hypervisor** (virtual machine monitor, VMM) is software that creates and runs virtual "
     "machines. It shares the physical CPU, memory, disks and network among them and keeps them isolated "
     "from each other."),
    ("p",
     "**Type 1 (bare-metal)** – the hypervisor is installed **directly on the physical hardware**, "
     "without a host operating system. It is itself a minimal operating system with direct access to the "
     "hardware, and it relies on hardware-assisted virtualisation (Intel VT-x / AMD-V). "
     "Examples: VMware ESXi, Microsoft Hyper-V, Xen, KVM."),
    ("p",
     "**Type 2 (hosted)** – the hypervisor is an **application installed on an existing operating "
     "system** (Windows, macOS, Linux). It depends fully on the host OS for access to the CPU, memory, "
     "disks and devices. Examples: Oracle VirtualBox, VMware Workstation, VMware Fusion, Parallels "
     "Desktop."),
    ("p",
     "**Server designed** – complete virtualisation **platforms built for servers and data centres**. "
     "They are usually based on a Type 1 hypervisor and add central management of many hosts, clustering, "
     "high availability (HA), live migration of running VMs, shared storage, virtual networking and "
     "backup. This category describes what the product is for (running a whole infrastructure), not where "
     "the hypervisor sits. Examples: VMware vSphere (ESXi + vCenter), Hyper-V with Windows Server "
     "Failover Clustering, Proxmox VE, XCP-ng/XenServer, Nutanix AHV."),

    ("h2", "2. Main differences"),
    ("table", "Table 1. Type 1 vs Type 2 vs server designed.",
     ["", "Type 1", "Type 2", "Server designed"],
     [
         ["Runs on", "Hardware directly", "Host operating system", "Cluster of servers (Type 1 underneath)"],
         ["Performance", "Near-native", "Lower (host OS overhead)", "Near-native"],
         ["Hardware support", "Limited (certified hardware)", "Wide (anything the host OS supports)",
          "Limited (certified servers)"],
         ["Security", "High, small attack surface", "Depends on the host OS", "High + access control, audit"],
         ["Setup / management", "Installed like an OS, managed remotely", "Installed like a program, local GUI",
          "Complex; central console for many hosts"],
         ["Scale", "Many VMs on one host", "A few VMs on a PC", "Hundreds of VMs on many hosts"],
         ["Cost", "Often paid (free options exist)", "Mostly free", "Highest (except open-source options)"],
     ],
     [3.0, 4.2, 4.2, 4.6]),

    ("h2", "3. Advantages and disadvantages"),
    ("table", "Table 2. Pros and cons.",
     ["Type", "Pros", "Cons"],
     [
         ["Type 1",
          ["Best performance", "Secure and stable (24/7)", "Scales to many VMs"],
          ["Needs a dedicated machine", "Limited hardware support", "Harder to set up and administer"]],
         ["Type 2",
          ["Very easy to install and use", "Runs on almost any PC", "Usually free; snapshots, shared folders"],
          ["Slower, especially disk and network", "If the host OS fails or is attacked, so are the VMs",
           "Not for production servers"]],
         ["Server designed",
          ["High availability, live migration", "Central management and automation",
           "Uses the whole infrastructure efficiently"],
          ["Expensive (commercial products)", "Needs several servers and shared storage",
           "Complex; needs skilled admins"]],
     ],
     [3.0, 6.5, 6.5]),

    ("h2", "4. When to use which"),
    ("bullets", [
        "**Type 1** – a dedicated server running production services that must be fast and secure, "
        "e.g. a company's database, mail or file server, or a hosting provider.",
        "**Type 2** – virtual machines as a tool on your own computer: learning (e.g. Linux on a Windows "
        "laptop for OS classes), software development and testing, running Windows apps on a Mac, old "
        "software, or safely opening suspicious files.",
        "**Server designed** – a company running many VMs on several servers that must not go down: data "
        "centres, private clouds, virtual desktops (VDI). Proxmox VE or XCP-ng are free options for small "
        "firms and home labs.",
    ]),
    ("p",
     "**Note:** KVM and Hyper-V are borderline cases. Both are enabled inside an existing OS (Linux or "
     "Windows), but they then run beneath it and control the hardware directly, so they are usually "
     "classified as Type 1."),

    ("h2", "Sources"),
    ("refs", [
        "Hypervisor wirtualizacyjny typu 1 oraz typu 2 – co je różni?, magnifier.pl, 2020, "
        "https://magnifier.pl/hypervisor-typ-1-typ-2-porownanie/",
        "Bilski P., Systemy operacyjne – Ćwiczenia 3: Wirtualizator Hyper-V (lecture slides).",
    ]),
]
