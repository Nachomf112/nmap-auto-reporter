# Nmap Auto Reporter

Herramienta en línea de comandos para lanzar escaneos **Nmap** y generar
un informe en **Markdown** listo para pegar en un ticket del SOC o en un informe.

## Características

- Lanza Nmap con detección de servicios (`-sV`) y perfil agresivo (`-T4`).
- Guarda el resultado en texto plano (`reports/scan_YYYYMMDD-HHMMSS.nmap`).
- Genera un informe Markdown con:
  - Fecha del escaneo (UTC).
  - Objetivo escaneado.
  - Comando Nmap utilizado.
  - Salida completa de Nmap en un bloque de código.

### Requisitos

- Linux (probado en Kali).
- Python 3.10+.
- Nmap instalado:

```bash
sudo apt update
sudo apt install nmap


pega esto:

```md
### Uso rápido

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/Nachomf112/nmap-auto-reporter.git
cd nmap-auto-reporter

