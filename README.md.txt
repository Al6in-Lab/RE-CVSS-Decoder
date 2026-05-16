# RE — CVSS Decoder Framework v1.0.0
A lightweight, high-utility command-line interface (CLI) tool designed to instantly parse, translate, and log CVSS (Common Vulnerability Scoring System) vector strings across versions 2.0, 3.x, and 4.0.

Built to accelerate triage workflows for security analysts by translating abstract technical vectors into actionable human-readable threat intelligence summaries.

## 🔍 Why This Matters (SOC Application)
During an incident triage or vulnerability assessment, analysts are constantly inundated with raw vectors like `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H`. Reading these manually slows down response times. 

**RE** solves this problem by:
1. **Instantly Decoding Metrics**: Translating shorthand values (e.g., `AV:N` ➔ `Attack Vector: Network`).
2. **Generating Natural Language Summaries**: Combining multi-variable metrics into cohesive risk descriptions.
3. **Automated Auditing**: Saving clean, plain-text logs into an isolated `/Bin` directory for archival and reporting purposes.

## 🚀 Features
* **Cross-Version Support**: Handles legacy CVSS v2.0, standard v3.x, and the modern split-impact structures introduced in CVSS v4.0.
* **Granular Risk Visualization**: Implements contextual ANSI color-coding (Red/Yellow/Green) to draw immediate attention to critical technical impacts (e.g., High/Complete privileges or impacts).
* **Cross-Platform Compatibility**: Features native Win32 API hooks to support full ANSI color maps within legacy Windows Command Prompt environments out-of-the-box.
* **Extensible Architecture**: Utilises nested lookup dictionaries to decouple data structures from operational parsing logic.

## ⚙️ How It Works
The engine relies on a clean, scalable nested dictionary architecture. The logic isolates the metric code from the risk value, allowing it to correctly identify value definitions dynamically depending on the metric context (e.g., handling `N` as "Network" in `AV` vs. "None" in `PR`).

```text
==================================================
  _____  ______     [ RE: CVSS Decoder Framework ]



 |  __ \|  ____|    
 | |__) | |__       [ Version: 1.0.0             ]
 |  _  /|  __|      [ Codename: Reverse          ]
 | | \ \| |____     
 |_|  \_\______|    Type 'exit' to close console.
==================================================

re_v4_decoder > CVSS:4.0/AV:N/AC:L/AT:N/PR:H/UI:N/VC:N/VI:N/VA:N/SC:H/SI:H/SA:H

[+] Successfully extracted telemetry data:
  » Target framework verified: CVSS v4.0
  » AV: Network
  » AC: Low
  » AT: None
  » PR: High
  » UI: None
  » VC: None
  » VI: None
  » VA: None
  » SC: High
  » SI: High
  » SA: High

[INFO] Automated Intelligence Report:
This vulnerability can be exploited over the Network with high privileges required and requires zero user interaction.
On the target system, it causes a none impact on confidentiality, a none impact on integrity, and a none impact on availability. It also ripples out to subsequent systems causing a high confidentiality impact, high integrity impact, and high availability impact.

[💾] Log block written to: Bin\cvss_result_1.txt
```

## 🛠️ Installation & Usage
No third-party packages or external dependencies required. 

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd RE-CVSS-Decoder
   ```
2. Run the tool natively using Python 3:
   ```bash
   python re_decoder.py
   ```

## ⚙️ Optional: System Shortcut Setup (Quality of Life)
To maintain the security integrity of the host machine, **RE** operates entirely in user space as a Proof of Concept (PoC) and does not automatically alter system paths. If you want to invoke **RE** natively from any directory using just the `RE` command, configure the environmental shortcuts manually:

### For Linux / macOS (Shell Alias)
Add a permanent alias to your shell profile configuration file (`~/.bashrc` or `~/.zshrc`):
1. Open the file: `nano ~/.bashrc`
2. Append the shortcut: `alias RE="python3 /absolute/path/to/re_decoder.py"`
3. Apply changes: `source ~/.bashrc`

### For Windows Environments (Batch Wrapper & PATH Entry)
1. Create a text file named exactly `RE.bat` inside your project folder.
2. Add this single line inside it to automatically forward terminal arguments to the engine:
   ```cmd
   @python "%~dp0re_decoder.py" %*
   ```
3. Open your Windows **Environment Variables** manager, select the **Path** user variable, and add the directory path where your files are stored. 

Open a fresh shell, type `RE`, and the framework will spin up globally.

## 📝 Project Evolution
* **Core Parsing & Data Architecture**: Independently designed and structured to showcase core logic mapping capabilities using native Python data structures.
* **Interface Polishing**: Augmented with AI assistance to efficiently incorporate ANSI styling definitions, automated directory bindings, and platform-specific kernel adjustments.

