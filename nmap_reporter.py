#!/usr/bin/env python3
# Nmap Auto Reporter - versión 0.1
# CLI para lanzar un escaneo Nmap y generar un informe en Markdown.

import datetime
import pathlib
import subprocess


def run_scan(target: str) -> tuple[pathlib.Path, pathlib.Path] | None:
    """Lanza Nmap contra 'target' y devuelve rutas de (scan, report)."""
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    reports_dir = pathlib.Path("reports")
    reports_dir.mkdir(exist_ok=True)

    normal_path = reports_dir / f"scan_{timestamp}.nmap"
    report_path = reports_dir / f"report_{timestamp}.md"

    cmd = ["nmap", "-sV", "-T4", "-Pn", "-oN", str(normal_path), target]

    print(f"[+] Ejecutando: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError:
        print("[-] nmap no está instalado. Instálalo con: sudo apt install nmap")
        return None
    except subprocess.CalledProcessError as e:
        print(f"[-] Error ejecutando nmap: {e}")
        return None

    print(f"[+] Escaneo terminado. Generando informe Markdown…")

    scan_text = normal_path.read_text(encoding="utf-8", errors="ignore")

    with report_path.open("w", encoding="utf-8") as f:
        f.write("# Nmap Report\n\n")
        f.write(f"- Fecha (UTC): {timestamp}\n")
        f.write(f"- Objetivo: `{target}`\n")
        f.write(f"- Comando: `{' '.join(cmd)}`\n\n")
        f.write("## Resultado bruto\n\n```nmap\n")
        f.write(scan_text)
        f.write("\n```\n")

    return normal_path, report_path


def main() -> None:
    print("=== Nmap Auto Reporter (v0.1) ===")
    target = input("Objetivo (IP o dominio): ").strip()

    if not target:
        print("[-] Debes indicar un objetivo.")
        return

    result = run_scan(target)
    if not result:
        return

    normal_path, report_path = result
    print(f"[+] Escaneo guardado en: {normal_path}")
    print(f"[+] Informe Markdown: {report_path}")
    print("[+] Listo para adjuntar al ticket del SOC o informe.")


if __name__ == "__main__":
    main()
