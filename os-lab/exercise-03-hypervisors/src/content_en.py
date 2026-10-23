TITLE_PAGE = {
    "university": "[[University name]]",
    "faculty": "[[Faculty / Department]]",
    "course": "Operating Systems",
    "exercise": "Exercise 3 – Hyper-V virtualiser and comparison of virtualisers available on the market",
    "title": "Type 1 and Type 2 Hypervisors",
    "subtitle": "Definitions, differences, advantages and disadvantages, applications, "
    "and an overview of Type 1, Type 2 and server-designed virtualisers",
    "fields": [
        ("Author", "[[First name Last name]]"),
        ("Student ID", "[[000000]]"),
        ("Group", "[[Group]]"),
        ("Lecturer", "mgr inż. Piotr Bilski"),
    ],
    "place_date": "[[City]], [[date]]",
}

BODY = [
    # ------------------------------------------------------------------ 1
    ("h1", "1. Introduction"),
    ("p",
     "**Virtualisation** is a technique that separates software from the physical hardware it runs on. "
     "A thin layer of software creates an abstraction of the processor, memory, storage and network "
     "devices, so that several isolated **virtual machines (VMs)** – each with its own operating system "
     "(the **guest OS**) – can run at the same time on one physical computer (the **host**)."),
    ("p",
     "The component that makes this possible is the **hypervisor**, also called the **virtual machine "
     "monitor (VMM)**. Its tasks are: allocating CPU time, memory and I/O devices to the virtual machines, "
     "isolating the VMs from each other and from the host, intercepting privileged instructions issued by "
     "guest operating systems, and controlling communication between the VMs and the physical hardware."),
    ("p",
     "The classification of hypervisors into **Type 1** and **Type 2** was introduced by Robert P. Goldberg "
     "in 1973 [3] and is still the standard way of describing them. The criterion is simple: **where the "
     "hypervisor sits relative to the hardware and the operating system**. A Type 1 hypervisor runs "
     "directly on the hardware, while a Type 2 hypervisor runs as an application on top of an existing "
     "operating system (Figure 1)."),
    ("p",
     "Modern x86 processors include hardware support for virtualisation – **Intel VT-x** and **AMD-V** "
     "(CPU virtualisation), **EPT/NPT** (also called SLAT – hardware translation of guest memory "
     "addresses) and **VT-d/AMD-Vi** (IOMMU, used to assign physical devices directly to a VM). These "
     "extensions are required by most current Type 1 hypervisors and are also used by Type 2 hypervisors, "
     "which greatly reduces the performance gap that existed when virtualisation relied only on software "
     "techniques such as binary translation [1][2]."),
    ("figure", "diagram_{lang}.png",
     "Figure 1. Architecture of a Type 1 (left) and a Type 2 (right) hypervisor. Own work based on [1]."),

    # ------------------------------------------------------------------ 2
    ("h1", "2. Type 1 hypervisor (bare-metal, native)"),
    ("h2", "2.1. Definition"),
    ("p",
     "A **Type 1 hypervisor** is installed **directly on the physical hardware** (\"bare metal\") instead "
     "of on an operating system. It is itself a specialised, minimal operating system whose only job is to "
     "run virtual machines. It has **direct access to hardware resources**, without an intermediate "
     "general-purpose operating system and its drivers. It uses full virtualisation with hardware "
     "acceleration, which it needs to work correctly [1]."),
    ("p",
     "In some designs a privileged management VM sits beside the hypervisor and supplies the device "
     "drivers and management tools: **dom0** in Xen and the **root (parent) partition** in Microsoft "
     "Hyper-V. Even then the hypervisor runs underneath all operating systems, including the management "
     "one, so the design is still Type 1."),
    ("h2", "2.2. Capabilities"),
    ("bullets", [
        "Near-native performance, because no host OS sits between the VMs and the hardware.",
        "Running dozens or hundreds of VMs on one server (server consolidation).",
        "Advanced memory management: overcommitment, page sharing, ballooning and compression.",
        "Live migration of a running VM between physical hosts without stopping it "
        "(e.g. vMotion, Hyper-V Live Migration).",
        "High availability (HA) and clustering: VMs restart automatically on another host after a failure.",
        "Direct hardware assignment: PCI passthrough, SR-IOV network cards, GPU sharing or passthrough "
        "(e.g. for VDI or AI workloads).",
        "Remote, centralised management of many hosts through web consoles and APIs.",
        "Strong isolation and a small attack surface, because the hypervisor's code base is small.",
    ]),
    ("h2", "2.3. Limitations"),
    ("bullets", [
        "**Limited hardware support.** No general-purpose OS supplies drivers, so the hypervisor runs only "
        "on certified hardware listed in its hardware compatibility list (HCL), which is especially true "
        "for VMware ESXi [1].",
        "**Needs a dedicated machine.** The hypervisor replaces the operating system, so the machine "
        "cannot also serve as an ordinary desktop.",
        "**Harder to install and administer.** It requires knowledge of networking, storage and remote "
        "management tools.",
        "**Licensing cost.** Commercial enterprise editions (VMware vSphere, Windows Server Datacenter) can "
        "be expensive, although free open-source options exist (KVM, Xen, Proxmox VE, XCP-ng).",
        "**Usually managed from another computer.** Day-to-day management needs a separate computer with "
        "a browser or console.",
    ]),
    ("h2", "2.4. Applications"),
    ("bullets", [
        "Data centres and server rooms: consolidating many physical servers onto a few hosts.",
        "Public and private clouds (IaaS): AWS (the Nitro hypervisor is based on KVM), Google Cloud (KVM), "
        "Microsoft Azure (Hyper-V), and OpenStack-based clouds.",
        "Production company workloads: domain controllers, databases, mail, ERP and file servers.",
        "Virtual Desktop Infrastructure (VDI): many user desktops served from central servers.",
        "Hosting and VPS providers, telecoms (NFV – network function virtualisation) and edge computing.",
        "Disaster recovery: replicating VMs to a second site (e.g. Hyper-V Replica, vSphere Replication).",
    ]),
    ("procon", "Table 1. Advantages and disadvantages of Type 1 hypervisors.",
     "Advantages", [
         "Highest performance and efficient use of resources",
         "Better security: small attack surface, does not inherit the vulnerabilities of a desktop OS",
         "Stability and reliability – designed for 24/7 operation",
         "Scalability: many VMs per host, clusters of many hosts",
         "Enterprise features: live migration, HA, load balancing, replication",
         "Centralised remote management and automation (APIs, PowerShell, Ansible)",
     ],
     "Disadvantages", [
         "Limited range of supported hardware (HCL)",
         "Needs a dedicated physical machine",
         "More complex installation, configuration and administration",
         "Commercial licences can be expensive",
         "Requires a separate management workstation or console",
         "A misconfiguration or failure of the host affects all of its VMs",
     ]),

    # ------------------------------------------------------------------ 3
    ("h1", "3. Type 2 hypervisor (hosted)"),
    ("h2", "3.1. Definition"),
    ("p",
     "A **Type 2 hypervisor** is an **application installed on an existing operating system** (the host "
     "OS), just like any other program. It is **fully dependent on the host OS**, which it uses to manage "
     "CPU scheduling, RAM, disk reads and writes, and access to devices. Because the host OS handles the "
     "hardware, the hypervisor can run on almost any computer that the OS supports. The cost is lower "
     "performance, since every guest operation passes through an additional layer [1]."),
    ("p",
     "Type 2 hypervisors also use hardware acceleration (VT-x/AMD-V) when it is available. Some of them "
     "can fall back to software techniques such as binary translation or full emulation (QEMU TCG) when "
     "the hardware lacks the needed features [1]."),
    ("h2", "3.2. Capabilities"),
    ("bullets", [
        "Quick installation – a few minutes, like any other application; no dedicated machine needed.",
        "Runs on ordinary laptops and desktops with Windows, macOS or Linux, so it supports a wide range of "
        "hardware.",
        "Host and guest systems work at the same time, side by side, on one screen.",
        "Desktop integration features: shared folders, a shared clipboard, drag-and-drop, USB device "
        "redirection, seamless or unity mode (guest application windows on the host desktop) and 3D "
        "graphics acceleration.",
        "Snapshots and clones, so it is easy to go back to a known state – ideal for experiments.",
        "Flexible virtual networking: NAT, bridged, host-only and internal networks.",
        "Some products (QEMU) can emulate a different CPU architecture, e.g. ARM or RISC-V on an x86 PC.",
    ]),
    ("h2", "3.3. Limitations"),
    ("bullets", [
        "**Lower performance**, especially for disk and network I/O, because requests pass through the host "
        "OS and its drivers. VMs also compete with host applications for CPU and RAM.",
        "**Security depends on the host OS.** If the host is compromised, all VMs are compromised. The "
        "attack surface is larger (host OS plus hypervisor application). Vulnerabilities in emulated "
        "devices, such as VENOM (CVE-2015-3456) in QEMU's virtual floppy controller, can allow a "
        "\"VM escape\".",
        "**Stability depends on the host.** Host OS updates, restarts or crashes stop every VM.",
        "**Limited scalability.** Typically a few VMs per host, with no clustering, HA or live migration "
        "between hosts.",
        "**Conflicts between hypervisors.** On Windows, enabling Hyper-V (also used by WSL 2 and "
        "virtualisation-based security) means that VirtualBox and VMware Workstation must run through the "
        "Windows Hypervisor Platform API, which can reduce their performance.",
        "**Not suitable for production servers** that must run 24/7.",
    ]),
    ("h2", "3.4. Applications"),
    ("bullets", [
        "Education: learning operating systems (e.g. installing Linux on a Windows laptop for OS classes) "
        "and building lab networks.",
        "Software development and testing on several operating systems or versions, and reproducing bugs.",
        "Running applications that need a different OS (e.g. Windows programs on a Mac).",
        "Running legacy software that does not work on a modern OS (e.g. an old Windows XP application).",
        "Security: safely opening suspicious files, malware analysis in an isolated VM with snapshots, and "
        "penetration-testing distributions (Kali Linux).",
        "Demos, training, proofs of concept and quickly trying out new systems.",
    ]),
    ("procon", "Table 2. Advantages and disadvantages of Type 2 hypervisors.",
     "Advantages", [
         "Very easy to install and use (graphical interface)",
         "Works on almost any computer – wide hardware compatibility",
         "No dedicated machine needed; host and guests work at the same time",
         "Mostly free (VirtualBox, VMware Workstation Pro/Fusion Pro, QEMU)",
         "Convenient desktop integration (clipboard, shared folders, USB)",
         "Snapshots make experiments safe and repeatable",
     ],
     "Disadvantages", [
         "Lower performance, especially for I/O; overhead from the host OS",
         "Security and stability depend on the host OS",
         "VMs compete with host applications for resources",
         "Poor scalability; no HA, clustering or live migration",
         "Possible conflicts with other hypervisors (e.g. Hyper-V on Windows)",
         "Not suitable for production server workloads",
     ]),

    # ------------------------------------------------------------------ 4
    ("h1", "4. Differences between Type 1 and Type 2 hypervisors"),
    ("p",
     "Table 3 summarises the main differences. The basic difference is the hypervisor's position in the "
     "software stack: **a Type 1 hypervisor controls the hardware itself, while a Type 2 hypervisor asks "
     "the host operating system for access to it**. Most of the other differences follow from this."),
    ("table", "Table 3. Comparison of Type 1 and Type 2 hypervisors.",
     ["Criterion", "Type 1 (bare-metal)", "Type 2 (hosted)"],
     [
         ["Position in the stack", "Directly on the hardware; it is the OS for the VMs",
          "Application or process running on a host OS"],
         ["Hardware access", "Direct (own drivers or a privileged partition such as dom0 or the root partition)",
          "Indirect – through host OS drivers"],
         ["Performance", "Near-native, low overhead", "Lower, especially I/O; extra layer and contention"],
         ["Hardware compatibility", "Limited – certified hardware (HCL)", "Broad – anything the host OS supports"],
         ["Security / isolation", "High; small attack surface", "Depends on the host OS; larger attack surface"],
         ["Stability", "Independent of a desktop OS; built for 24/7", "Host updates or crashes stop the VMs"],
         ["Installation", "Installed like an OS on a dedicated machine", "Installed like an ordinary program"],
         ["Management", "Remote, centralised (web GUI, vCenter, SCVMM, APIs)", "Local GUI on the same computer"],
         ["Scalability", "Tens to hundreds of VMs per host; clusters", "A few VMs; single computer"],
         ["Typical features", "Live migration, HA, clustering, replication, passthrough, SR-IOV",
          "Snapshots, shared folders, clipboard, USB, seamless mode"],
         ["Cost", "Often paid licence or subscription (free options exist)", "Mostly free"],
         ["Typical users", "Data centres, cloud providers, companies", "Students, developers, testers, home users"],
         ["Examples", "VMware ESXi, Microsoft Hyper-V, Xen, KVM*",
          "Oracle VirtualBox, VMware Workstation and Fusion, Parallels Desktop, QEMU"],
     ],
     [3.6, 6.2, 6.2]),
    ("p",
     "* **Borderline cases.** **KVM** (Kernel-based Virtual Machine) is a Linux kernel module. At first "
     "sight it looks like a Type 2 hypervisor because it is loaded into an ordinary Linux system. However, "
     "it turns the Linux kernel itself into a hypervisor, so many sources (e.g. Red Hat) classify it as "
     "Type 1. Others, including the article used in class, describe it as Type 2, because a full Linux "
     "system provides the virtualisation, not only the kernel [1][6]. **Microsoft Hyper-V** is the opposite "
     "case. It is installed as a Windows Server role or Windows feature, so it seems to be an "
     "application. However, enabling it places the hypervisor beneath Windows, and Windows then becomes "
     "the root partition running on top of it. Hyper-V is therefore a Type 1 hypervisor [1][5]."),

    # ------------------------------------------------------------------ 5
    ("h1", "5. When to use which type"),
    ("p",
     "A simple rule is: **use Type 1 when virtual machines are the product** (production services that "
     "must be fast, secure and always available), and **use Type 2 when virtual machines are a tool** "
     "(for learning, development, testing or occasionally running another OS on your own computer). "
     "Table 4 shows typical scenarios."),
    ("table", "Table 4. Recommended hypervisor type for typical scenarios.",
     ["Scenario", "Recommended", "Justification"],
     [
         ["Company production servers (AD, databases, mail, ERP)", "Type 1 / server-designed platform",
          "Performance, 24/7 reliability, HA, backup and central management"],
         ["Cloud provider, hosting, VPS", "Type 1 (KVM, Xen, Hyper-V) in a cloud platform",
          "Very high VM density, multi-tenancy, automation through APIs"],
         ["Virtual desktops (VDI) for employees", "Type 1 / server-designed platform",
          "Many desktops from central servers; GPU sharing"],
         ["Consolidating old physical servers", "Type 1",
          "Fewer machines, lower power and cooling costs, easier management"],
         ["Small branch office or edge site (2–3 servers)", "Type 1 (Hyper-V, Proxmox VE, small HCI)",
          "Reliability with a small hardware footprint"],
         ["Student running Linux on a Windows laptop for OS classes", "Type 2 (VirtualBox, VMware Workstation)",
          "Free, quick to install, host stays usable; snapshots allow safe experiments"],
         ["Developer testing an application on many OSes", "Type 2",
          "Quickly creating, cloning and resetting test VMs"],
         ["Mac user who needs Windows applications", "Type 2 (Parallels Desktop, VMware Fusion)",
          "Good integration with the macOS desktop"],
         ["Analysing suspicious files or malware", "Type 2 with snapshots and an isolated network "
          "(dedicated Type 1 host for a professional lab)",
          "Easy rollback; the threat is kept away from the host"],
         ["Running old (legacy) software", "Type 2", "Old OS in a VM without dedicating a whole machine"],
         ["Emulating another CPU architecture (ARM, RISC-V)", "QEMU (Type 2 emulator)",
          "Only an emulator can run code for a different instruction set"],
         ["Home lab for learning server administration", "Server-designed (Proxmox VE, XCP-ng) on a spare PC",
          "Learning clustering, HA and storage like in a real company, at no cost"],
     ],
     [5.2, 4.8, 6.0]),

    # ------------------------------------------------------------------ 6
    ("h1", "6. Server-designed virtualisers"),
    ("h2", "6.1. Definition"),
    ("p",
     "**Server-designed virtualisers** (server-class or enterprise virtualisation platforms) are complete "
     "virtualisation solutions designed from the start to run **production workloads on servers and in "
     "data centres**, typically on **many physical hosts managed as one pool of resources**. In addition "
     "to the hypervisor they provide a whole ecosystem: central management, clustering, high "
     "availability, live migration, shared or software-defined storage and networking, backup, monitoring, "
     "user roles and permissions, and an API for automation."),
    ("p",
     "This category is **not a third position in the stack** next to Type 1 and Type 2. It describes the "
     "**purpose and scope** of a product, not where the hypervisor sits. In practice almost every "
     "server-designed platform is built on a **Type 1 hypervisor** (ESXi, Hyper-V, Xen or KVM). The "
     "difference is that a Type 1 hypervisor alone virtualises a single machine, while a server-designed "
     "platform manages a whole infrastructure. For example, ESXi is the hypervisor, and vSphere (ESXi + "
     "vCenter) is the server platform."),
    ("h2", "6.2. Characteristic features"),
    ("bullets", [
        "**Central management** of many hosts and VMs from one console (vCenter, System Center VMM / Windows "
        "Admin Center, Proxmox web GUI, Xen Orchestra, Nutanix Prism).",
        "**Clusters and high availability (HA)**: when a host fails, its VMs restart automatically on the "
        "remaining hosts.",
        "**Live migration** of running VMs and their storage between hosts, e.g. for hardware maintenance "
        "without downtime.",
        "**Automatic load balancing** (e.g. VMware DRS) and resource pools with quotas.",
        "**Software-defined storage and hyperconvergence (HCI)**: vSAN, Storage Spaces Direct, Ceph or ZFS "
        "– local disks of many servers combined into shared, redundant storage.",
        "**Software-defined networking (SDN)**: virtual switches, VLANs and VXLANs, microsegmentation, "
        "firewalls.",
        "**Backup, replication and disaster recovery** integration; templates and fast provisioning.",
        "**Security and compliance**: role-based access control (RBAC), audit logs, encrypted or shielded "
        "VMs, TPM emulation and Secure Boot.",
        "**Automation**: REST APIs, PowerShell/PowerCLI, Terraform, Ansible; often vendor support and "
        "certifications.",
    ]),
    ("procon", "Table 5. Advantages and disadvantages of server-designed virtualisers.",
     "Advantages", [
         "Highest availability – HA and live migration minimise downtime",
         "Efficient use of the whole infrastructure (consolidation, load balancing)",
         "Central management and automation of hundreds of VMs",
         "Built-in or integrated storage, networking, backup and DR",
         "Vendor support, certifications and a large ecosystem",
         "Scales from a few servers to a whole data centre",
     ],
     "Disadvantages", [
         "Highest cost (licences or subscriptions, often per CPU core) for commercial products",
         "Requires several servers, shared storage and fast networks for full functionality",
         "High complexity; requires qualified administrators",
         "Risk of vendor lock-in (e.g. the VMware licensing changes after 2023)",
         "Too much for a single computer or a home user (except open-source platforms used in home labs)",
     ]),
    ("h2", "6.3. When to use"),
    ("p",
     "Server-designed platforms are the right choice whenever a company runs **production services** that "
     "must be available all the time and are spread across **more than one physical server**. Examples "
     "are company data centres, private clouds, hosting, VDI and branch offices that need high "
     "availability. Smaller organisations and home labs increasingly use open-source platforms such as "
     "Proxmox VE or XCP-ng, which offer clustering and HA without licence fees."),

    # ------------------------------------------------------------------ 7
    ("h1", "7. Overview of virtualisers available on the market"),
    ("p",
     "The following sections describe the most popular products, divided into three groups, as the "
     "exercise requires. Group A contains the Type 1 hypervisors themselves, group B contains Type 2 "
     "(hosted) products, and group C contains complete server-designed platforms, most of which are built "
     "on the hypervisors from group A."),

    ("h2", "7.1. Group A – Type 1 hypervisors"),
    ("h3", "VMware ESXi (Broadcom)"),
    ("p",
     "ESXi is a mature, widely used bare-metal hypervisor with its own small kernel (VMkernel). It installs "
     "on a server, is managed through a web-based Host Client or centrally through vCenter, and supports "
     "very large VMs, memory overcommitment, PCI passthrough and vGPU. **Capabilities:** very high "
     "performance and stability, and a huge ecosystem of backup and monitoring tools. **Limitations:** "
     "strict hardware compatibility list. After Broadcom acquired VMware in 2023, licensing changed to "
     "subscription bundles, which significantly raised costs for many customers. **Use:** enterprise data "
     "centres, as the basis of the vSphere platform (group C)."),
    ("h3", "Microsoft Hyper-V"),
    ("p",
     "Hyper-V is Microsoft's Type 1 hypervisor, available as a role in Windows Server and as an optional "
     "feature of Windows 10/11 Pro, Enterprise and Education. It requires a 64-bit CPU with SLAT and "
     "hardware virtualisation enabled. Windows runs in the root partition, and VMs run in child "
     "partitions. **Capabilities:** Generation 1 and Generation 2 VMs (UEFI, Secure Boot, virtual TPM), "
     "checkpoints, Live Migration, Hyper-V Replica, nested virtualisation, Discrete Device Assignment and "
     "GPU partitioning. It is also the basis of Microsoft Azure, WSL 2, Windows Sandbox and "
     "virtualisation-based security. **Limitations:** management is Windows-oriented (Hyper-V Manager, "
     "PowerShell, Windows Admin Center, SCVMM), the free stand-alone Hyper-V Server was discontinued after "
     "the 2019 version, and the Windows Home edition does not include it. **Use:** Windows-based "
     "companies, labs and developer workstations. It is the main subject of this course's laboratory."),
    ("h3", "Xen Project (Linux Foundation)"),
    ("p",
     "Xen is an open-source microkernel hypervisor created at the University of Cambridge (first release "
     "2003). The hypervisor itself is very small. A privileged domain, **dom0** (usually Linux), provides "
     "drivers and management, and guests run as **domU** domains. Xen pioneered **paravirtualisation (PV)**, "
     "and also supports HVM and PVH guests. **Capabilities:** strong isolation and a small trusted code "
     "base, and it is also used in embedded and automotive systems. **Limitations:** configuration without "
     "a management platform is demanding. **Use:** AWS EC2 for many years, plus XenServer, XCP-ng and "
     "Qubes OS (a security-focused desktop OS)."),
    ("h3", "KVM – Kernel-based Virtual Machine"),
    ("p",
     "KVM has been part of the Linux kernel since version 2.6.20 (2007). Loading the kvm module turns Linux "
     "into a hypervisor: every VM is an ordinary Linux process scheduled by the kernel. **QEMU** emulates "
     "the devices, **virtio** drivers give fast paravirtualised I/O, and **libvirt** / virt-manager / "
     "Cockpit provide management. **Capabilities:** open source (GPL), excellent performance, live "
     "migration, and it benefits from all Linux features (cgroups, SELinux/sVirt, filesystems). "
     "**Limitations:** on its own it has no central graphical management for many hosts and requires "
     "Linux knowledge. **Use:** the most widely used hypervisor in public clouds (Google Cloud, AWS Nitro, "
     "OpenStack). It is also the basis of Proxmox VE, Nutanix AHV and OpenShift Virtualization."),
    ("h3", "IBM z/VM and PowerVM"),
    ("p",
     "These are hypervisors for IBM mainframes (IBM Z) and IBM Power servers. z/VM descends from CP-67 and "
     "VM/370 (1960s–1970s), the first commercial virtual machine systems, which the Type 1 and Type 2 "
     "theory was originally based on. **Capabilities:** extreme reliability and thousands of Linux guests "
     "on one machine. **Limitations:** work only on IBM hardware and are very expensive. **Use:** banks, "
     "insurance companies and large enterprises."),

    ("h2", "7.2. Group B – Type 2 hypervisors"),
    ("h3", "Oracle VirtualBox"),
    ("p",
     "VirtualBox is a free, open-source (GPLv2) hosted hypervisor for Windows, Linux and macOS hosts "
     "(including Apple Silicon since version 7.1). **Capabilities:** supports many guest systems, "
     "snapshots, cloning, shared folders, NAT, bridged and internal networks, Guest Additions for desktop "
     "integration, and a command-line tool (VBoxManage). **Limitations:** lower 3D and I/O performance than "
     "commercial products, and the Extension Pack (USB 2/3 passthrough, disk encryption, etc.) is licensed "
     "only for personal and educational use. **Use:** the most popular choice for students, education, "
     "home users and quick tests."),
    ("h3", "VMware Workstation Pro"),
    ("p",
     "Workstation Pro is a professional Type 2 hypervisor for Windows and Linux. Since November 2024 it has "
     "been free for personal, educational and commercial use. **Capabilities:** very good performance and "
     "3D support, snapshot trees, linked clones, a virtual network editor, virtual TPM and encrypted VMs, "
     "and the ability to connect to ESXi/vSphere and move VMs to them. **Limitations:** proprietary, and "
     "only runs on x86 hosts. **Use:** developers, IT trainers and administrators preparing VMs for "
     "vSphere."),
    ("h3", "VMware Fusion Pro"),
    ("p",
     "Fusion Pro is the macOS version of Workstation, also free since November 2024. On Apple Silicon Macs "
     "it runs ARM guests (Windows 11 on Arm, ARM Linux). **Capabilities:** Unity mode, which shows guest "
     "application windows directly on the macOS desktop, and good integration with the VMware ecosystem. "
     "**Limitations:** on Apple Silicon it cannot run x86 operating systems efficiently. **Use:** Mac users "
     "who need Windows or Linux."),
    ("h3", "Parallels Desktop"),
    ("p",
     "Parallels Desktop is a commercial hypervisor for macOS. It uses Apple's Hypervisor.framework, and "
     "Microsoft has officially approved it for running Windows 11 on Arm on Apple M-series computers. "
     "**Capabilities:** very good performance and graphics, Coherence mode (Windows applications as if "
     "they were native Mac applications), and one-click installation of Windows, Linux and macOS guests. "
     "**Limitations:** paid subscription and macOS only. **Use:** Mac users running Windows software "
     "(office, engineering or games)."),
    ("h3", "QEMU (and front-ends such as UTM)"),
    ("p",
     "QEMU is an open-source machine emulator and virtualiser created by Fabrice Bellard in 2003. Without "
     "acceleration it works as a pure Type 2 **emulator** that uses dynamic binary translation (TCG), so it "
     "can run code for a **different CPU architecture** (ARM, RISC-V, PowerPC, MIPS) on an x86 PC. With "
     "acceleration (KVM on Linux, HVF on macOS, WHPX on Windows) it runs guests at near-native speed. "
     "**Limitations:** pure emulation is slow, and the command line is complex (front-ends such as "
     "virt-manager or UTM on macOS/iOS help). **Use:** embedded-systems and OS-kernel development, testing "
     "other architectures, CI pipelines, and as the device-emulation component of KVM."),

    ("h2", "7.3. Group C – Server-designed virtualisers"),
    ("h3", "VMware vSphere / VMware Cloud Foundation (Broadcom)"),
    ("p",
     "vSphere consists of ESXi hosts plus **vCenter Server**, the central management system. It is extended "
     "in VMware Cloud Foundation with vSAN (hyperconverged storage), NSX (network virtualisation) and "
     "automation tools. **Capabilities:** vMotion and Storage vMotion, HA, DRS load balancing, Fault "
     "Tolerance (a shadow copy of a VM running in lockstep), distributed switches, and a huge ecosystem. "
     "**Limitations:** high cost after the subscription-only licensing change in 2024, and vendor lock-in. "
     "**Use:** large enterprises, banks, public administration and service providers. It has long been "
     "the market reference point."),
    ("h3", "Microsoft Hyper-V on Windows Server and Azure Local"),
    ("p",
     "Hyper-V hosts combined with **Failover Clustering**, **Storage Spaces Direct** and management through "
     "System Center Virtual Machine Manager or Windows Admin Center form a complete server platform. "
     "**Azure Local** (formerly Azure Stack HCI) is Microsoft's hyperconverged system managed from the Azure "
     "cloud. **Capabilities:** clustered HA, Live Migration, Hyper-V Replica, SDN, shielded VMs, and close "
     "integration with Active Directory and Azure. **Use:** organisations based on Microsoft technologies, "
     "and hybrid cloud."),
    ("h3", "Proxmox Virtual Environment (Proxmox VE)"),
    ("p",
     "Proxmox VE is an open-source (AGPLv3) server platform based on Debian Linux, from Proxmox Server "
     "Solutions GmbH (Vienna). It combines **KVM** virtual machines and **LXC** containers and is managed "
     "through a web interface. **Capabilities:** multi-node clusters, HA, live migration, built-in **Ceph** "
     "and **ZFS** storage, a firewall, SDN, and integration with Proxmox Backup Server. **Limitations:** "
     "the stable enterprise repository and official support require a paid subscription, and it has a "
     "smaller ecosystem than VMware. **Use:** small and medium companies, schools and home labs. It is a "
     "popular alternative to VMware after 2024."),
    ("h3", "XenServer and XCP-ng"),
    ("p",
     "XenServer (formerly Citrix Hypervisor, Cloud Software Group) and its community fork **XCP-ng** "
     "(Vates) are server platforms based on the **Xen** hypervisor. XCP-ng is managed with **Xen "
     "Orchestra**. **Capabilities:** resource pools, HA, live migration including storage, backup, and "
     "strong Citrix VDI integration (XenServer). **Limitations:** a smaller community than KVM-based "
     "solutions. **Use:** VDI (Citrix Virtual Apps and Desktops), and companies looking for an open-source "
     "replacement for vSphere."),
    ("h3", "Nutanix AHV"),
    ("p",
     "AHV is a KVM-based hypervisor included in the **hyperconverged** Nutanix Cloud Infrastructure, "
     "managed through **Prism**. Compute and distributed storage run on the same nodes. **Capabilities:** "
     "simple one-click upgrades, HA, built-in replication and DR, and no separate hypervisor licence. "
     "**Limitations:** tied to the Nutanix software stack and certified hardware. **Use:** companies that "
     "want a simple, scalable private cloud. It is often chosen when migrating away from VMware."),
    ("h3", "OpenStack and OpenShift Virtualization (KubeVirt)"),
    ("p",
     "**OpenStack** is an open-source cloud platform (IaaS). Its Nova component manages hypervisors, most "
     "often KVM, across hundreds or thousands of servers, with self-service, multi-tenancy and APIs. "
     "**Red Hat OpenShift Virtualization**, based on the KubeVirt project, runs VMs next to containers "
     "inside Kubernetes. It is Red Hat's successor to the discontinued Red Hat Virtualization (oVirt). "
     "**Limitations:** both are very complex and require large teams to operate. **Use:** telecoms, "
     "research centres, public and private clouds, and companies modernising applications towards "
     "containers."),

    ("table", "Table 6. Summary of the virtualisers described.",
     ["Product", "Group / type", "Licence", "Host / platform", "Main use"],
     [
         ["VMware ESXi", "A – Type 1", "Proprietary", "Bare-metal x86 server", "Enterprise servers"],
         ["Microsoft Hyper-V", "A – Type 1", "Part of Windows / Windows Server", "Bare metal (Windows in root partition)",
          "Windows servers, labs, developers"],
         ["Xen Project", "A – Type 1", "Open source (GPLv2)", "Bare metal + dom0", "Clouds, security, embedded"],
         ["KVM", "A – Type 1*", "Open source (GPL)", "Linux kernel", "Public clouds, basis of many platforms"],
         ["IBM z/VM, PowerVM", "A – Type 1", "Proprietary", "IBM Z / Power", "Mainframes, large enterprises"],
         ["Oracle VirtualBox", "B – Type 2", "Open source + PUEL extension pack", "Windows, Linux, macOS",
          "Education, home users, tests"],
         ["VMware Workstation Pro", "B – Type 2", "Proprietary, free", "Windows, Linux", "Developers, trainers"],
         ["VMware Fusion Pro", "B – Type 2", "Proprietary, free", "macOS", "Mac users"],
         ["Parallels Desktop", "B – Type 2", "Commercial subscription", "macOS", "Windows apps on Mac"],
         ["QEMU / UTM", "B – Type 2 (emulator)", "Open source", "Linux, Windows, macOS", "Cross-architecture emulation"],
         ["VMware vSphere / VCF", "C – Server (ESXi)", "Subscription", "Server clusters", "Enterprise data centres"],
         ["Hyper-V + Failover Clustering / Azure Local", "C – Server (Hyper-V)", "Windows Server / Azure subscription",
          "Server clusters, HCI", "Microsoft environments, hybrid cloud"],
         ["Proxmox VE", "C – Server (KVM + LXC)", "Open source, optional subscription", "Server clusters",
          "SMEs, schools, home labs"],
         ["XenServer / XCP-ng", "C – Server (Xen)", "Commercial / open source", "Server pools",
          "VDI, vSphere alternative"],
         ["Nutanix AHV", "C – Server (KVM, HCI)", "Commercial", "Nutanix HCI nodes", "Private cloud"],
         ["OpenStack, OpenShift Virtualization", "C – Server / cloud (KVM)", "Open source / commercial",
          "Large clusters", "Private and public clouds"],
     ],
     [3.4, 2.8, 3.2, 3.3, 3.3]),

    # ------------------------------------------------------------------ 8
    ("h1", "8. Conclusions"),
    ("p",
     "Type 1 and Type 2 hypervisors are not competitors but tools for different jobs. A **Type 1** "
     "hypervisor runs directly on the hardware and offers the best performance, security and "
     "scalability, so it is the standard in data centres and clouds. Its costs are limited hardware "
     "support and more complex administration. A **Type 2** hypervisor is an application on an ordinary "
     "operating system. It is easy to install, free in most cases and works on almost any computer, which "
     "makes it ideal for learning, development and testing. It pays for this with lower performance and a "
     "dependence on the host OS."),
    ("p",
     "**Server-designed** virtualisers are complete platforms built around a Type 1 hypervisor. They "
     "move virtualisation from a single machine to the whole infrastructure, adding central management, "
     "clustering, high availability, live migration, and software-defined storage and networking. The "
     "boundaries between the categories are blurring: KVM and Hyper-V look like applications but work as "
     "Type 1 hypervisors, and Type 2 products such as VMware Workstation can connect to server platforms. "
     "The choice should therefore depend on what the virtual machines are for: **a tool on your own "
     "computer (Type 2)**, **a production service on a dedicated server (Type 1)** or **an entire "
     "infrastructure (server-designed platform)**."),

    # ------------------------------------------------------------------ refs
    ("h1", "References"),
    ("refs", [
        "Hypervisor wirtualizacyjny typu 1 oraz typu 2 – co je różni?, magnifier.pl, 6 September 2020, "
        "https://magnifier.pl/hypervisor-typ-1-typ-2-porownanie/",
        "Bilski P., Systemy operacyjne – Ćwiczenia 3: Wirtualizator Hyper-V (lecture slides).",
        "Goldberg R. P., Architectural Principles for Virtual Computer Systems, PhD thesis, Harvard "
        "University, 1973.",
        "Popek G. J., Goldberg R. P., Formal Requirements for Virtualizable Third Generation Architectures, "
        "Communications of the ACM, 17(7), 1974, pp. 412–421.",
        "Microsoft Learn, Hyper-V on Windows and Windows Server – documentation, "
        "https://learn.microsoft.com/virtualization/",
        "Red Hat, What is KVM?, https://www.redhat.com/en/topics/virtualization/what-is-KVM",
        "Broadcom, VMware vSphere / ESXi documentation, https://techdocs.broadcom.com/",
        "Xen Project, Xen Project Software Overview, https://xenproject.org/",
        "Oracle, Oracle VirtualBox User Manual, https://www.virtualbox.org/manual/",
        "Proxmox Server Solutions, Proxmox VE Administration Guide, https://pve.proxmox.com/pve-docs/",
        "QEMU Project, QEMU documentation, https://www.qemu.org/docs/master/",
        "Tanenbaum A. S., Bos H., Modern Operating Systems, 4th ed., Pearson, 2015 – Chapter 7: "
        "Virtualization and the Cloud.",
        "Silberschatz A., Galvin P. B., Gagne G., Operating System Concepts, 10th ed., Wiley, 2018 – "
        "Chapter 18: Virtual Machines.",
    ]),
]
