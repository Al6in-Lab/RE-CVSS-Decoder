import os
import sys

# --- Fix for Windows Terminal Colors ---
if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# --- RE Framework Colors ---
CLR_RESET = "\033[0m"
CLR_RED   = "\033[91m"   
CLR_YLW   = "\033[93m"   
CLR_GRN   = "\033[92m"   
CLR_CYAN  = "\033[96m"   

# Master Lookup Dictionary
cvss_lookup = {
    "AV": {"N": "Network", "A": "Adjacent", "L": "Local", "P": "Physical"},
    "AC": {"L": "Low", "H": "High"},
    "PR": {"N": "None", "L": "Low", "H": "High"},
    "UI": {"N": "None", "R": "Required", "A": "Active", "P": "Passive"},
    "S":  {"U": "Unchanged", "C": "Changed"},
    "Au": {"N": "None", "S": "Single", "M": "Multiple"},
    "C":  {"N": "None", "L": "Low", "H": "High", "P": "Partial", "C": "Complete"},
    "I":  {"N": "None", "L": "Low", "H": "High", "P": "Partial", "C": "Complete"},
    "A":  {"N": "None", "L": "Low", "H": "High", "P": "Partial", "C": "Complete"},
    "AT": {"N": "None", "H": "High"},
    "VC": {"N": "None", "L": "Low", "H": "High"},
    "VI": {"N": "None", "L": "Low", "H": "High"},
    "VA": {"N": "None", "L": "Low", "H": "High"},
    "SC": {"N": "None", "L": "Low", "H": "High"},
    "SI": {"N": "None", "L": "Low", "H": "High"},
    "SA": {"N": "None", "L": "Low", "H": "High"}
}

def get_color(value_text: str) -> str:
    lowered = value_text.lower()
    if lowered in ["high", "complete", "required", "active", "changed"]:
        return CLR_RED
    if lowered in ["low", "partial", "passive"]:
        return CLR_YLW
    return CLR_GRN

output_dir = "Bin"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- Wifite / Facad1ng Style Banner ---
banner = f"""{CLR_CYAN}==================================================
  _____  ______     {CLR_RESET}[ {CLR_GRN}RE: CVSS Decoder Framework{CLR_RESET} ]

 |  __ \\|  ____|    
 | |__) | |__       {CLR_RESET}[ {CLR_CYAN}Version: 1.0.0{CLR_RESET}             ]
 |  _  /|  __|      {CLR_RESET}[ {CLR_CYAN}Codename: Reverse{CLR_RESET}          ]
 | | \\ \\| |____     
 |_|  \\_\\______|    {CLR_RESET}Type '{CLR_RED}exit{CLR_RESET}' to close console.
=================================================={CLR_RESET}"""

print(banner)

file_counter = 1
while True:
    try:
        # Prompt styled like an active testing terminal
        user_input = input(f"\n{CLR_CYAN}re_v4_decoder > {CLR_RESET}").strip()
        
        if user_input.lower() == 'exit':
            print(f"[{CLR_RED}-{CLR_RESET}] Shutting down RE module. Goodbye!")
            break
            
        if not user_input:
            continue

        split_input = user_input.split("/")
        results = {}
        version = "2.0"
        
        terminal_output = []
        file_output = [f"Raw Vector: {user_input}\n", "-"*50 + "\n"]

        # Parse string metrics
        for item in split_input:
            if ":" in item:
                metric, value = item.split(":")
                
                if metric == "CVSS":
                    version = value
                    terminal_output.append(f"[{CLR_GRN}+{CLR_RESET}] Target framework verified: CVSS v{version}")
                    file_output.append(f"Target framework verified: CVSS v{version}\n")
                    continue
                
                if metric in cvss_lookup and value in cvss_lookup[metric]:
                    full_text = cvss_lookup[metric][value]
                    color = get_color(full_text)
                    
                    terminal_output.append(f"  {CLR_CYAN}»{CLR_RESET} {metric}: {color}{full_text}{CLR_RESET}")
                    file_output.append(f"  » {metric}: {full_text}\n")
                    results[metric] = full_text

        # Build access sentence strings
        access_msg = ""
        if "AV" in results:
            access_msg += f"This vulnerability can be exploited over the {results['AV']}"
            if "PR" in results:
                access_msg += f" with {results['PR'].lower()} privileges required"
            elif "Au" in results:
                access_msg += f" requiring {results['Au'].lower()} level of authentication"
            if "UI" in results:
                if results['UI'] in ["Required", "Active", "Passive"]:
                    access_msg += " and requires a user to interact with the exploit."
                else:
                    access_msg += " and requires zero user interaction."
            access_msg += " "

        # Build impact sentence strings
        impact_msg = ""
        if "VC" in results:
            impact_msg += f"On the target system, it causes a {results['VC'].lower()} impact on confidentiality, a {results['VI'].lower()} impact on integrity, and a {results['VA'].lower()} impact on availability. "
            if "SC" in results:
                impact_msg += f"It also ripples out to subsequent systems causing a {results['SC'].lower()} confidentiality impact, {results['SI'].lower()} integrity impact, and {results['SA'].lower()} availability impact."
        elif "C" in results:
            impact_msg += f"If successful, it causes a {results['C'].lower()} impact on confidentiality, a {results['I'].lower()} impact on integrity, and a {results['A'].lower()} impact on availability."

        summary_sentence = f"{access_msg.strip()}\n{impact_msg.strip()}".strip()

        # Display parsing summary framework style
        print(f"[{CLR_GRN}+{CLR_RESET}] Successfully extracted telemetry data:")
        for line in terminal_output:
            print(line)
            
        print(f"\n[{CLR_YLW}INFO{CLR_RESET}] Automated Intelligence Report:")
        print(f"{summary_sentence}")

        # File write execution
        file_name = f"cvss_result_{file_counter}.txt"
        file_path = os.path.join(output_dir, file_name)
        
        file_output.append("\n" + "="*50 + "\nAutomated Intelligence Report:\n" + summary_sentence + "\n")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(file_output)
            
        print(f"[{CLR_GRN}💾{CLR_RESET}] Log block written to: {CLR_GRN}{file_path}{CLR_RESET}")
        file_counter += 1

    except KeyboardInterrupt:
        print(f"\n\n[{CLR_RED}-{CLR_RESET}] Execution interrupted by operator. Exiting.")
        break
