# 🔍 Nmap Auto Reporter

> CLI en Python para lanzar escaneos Nmap y generar informes en Markdown listos para adjuntar a tickets SOC.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Nmap](https://img.shields.io/badge/Nmap-0E83CD?style=for-the-badge&logo=nmap&logoColor=white)
![Blue Team](https://img.shields.io/badge/Blue_Team-SOC-22c55e?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 ¿Qué hace?

**Nmap Auto Reporter** automatiza el flujo completo de escaneo y documentación:

```
Target (IP/dominio)
      ↓
Escaneo Nmap (-sV -T4 -Pn)
      ↓
Informe Markdown generado automáticamente
      ↓
Listo para ticket SOC / informe técnico
```

---

## ✅ Características

- Lanza Nmap con detección de servicios (`-sV`) y perfil agresivo (`-T4`).
- Guarda el resultado en texto plano (`reports/scan_YYYYMMDD-HHMMSS.nmap`).
- Genera un informe Markdown con:
  - Fecha del escaneo (UTC)
  - Objetivo escaneado
  - Comando Nmap utilizado
  - Salida completa de Nmap en bloque de código

---

## 🚀 Instalación

### Requisitos

- Linux (probado en Kali)
- Python 3.10+
- Nmap instalado

```bash
# Instalar Nmap
sudo apt update && sudo apt install nmap

# Clonar el repositorio
git clone https://github.com/Nachomf112/nmap-auto-reporter.git
cd nmap-auto-reporter
```

No requiere dependencias externas de Python — solo librería estándar.

---

## ▶️ Uso

```bash
python3 nmap_reporter.py
```

```
=== Nmap Auto Reporter (v0.1) ===
Objetivo (IP o dominio): 192.168.1.1
[+] Ejecutando: nmap -sV -T4 -Pn -oN reports/scan_20260505-143022.nmap 192.168.1.1
[+] Escaneo terminado. Generando informe Markdown…
[+] Escaneo guardado en: reports/scan_20260505-143022.nmap
[+] Informe Markdown: reports/report_20260505-143022.md
[+] Listo para adjuntar al ticket del SOC o informe.
```

---

## 📄 Ejemplo de salida real

Puedes ver un ejemplo real de informe generado en Markdown aquí:

- [Ejemplo de informe Nmap contra menarguez-ia.com](reports/ejemplo_scan_menarguez-ia.md)

---

## 📁 Estructura del proyecto

```
nmap-auto-reporter/
├── nmap_reporter.py      # Script principal
├── reports/              # Generado automáticamente
│   ├── scan_*.nmap       # Salida raw de Nmap
│   └── report_*.md       # Informe Markdown listo para SOC
├── requisitos.txt
└── README.md
```

---

## 🛡️ Casos de uso SOC

- ✅ Reconocimiento inicial de un activo durante un incidente
- ✅ Documentación rápida de puertos abiertos para tickets
- ✅ Auditorías internas de red con trazabilidad
- ✅ Prácticas en laboratorio CTF / homelab

> ⚠️ **Uso ético**: Lanza escaneos únicamente contra sistemas sobre los que tengas autorización explícita.

---

## 🗺️ Roadmap

- [x] Escaneo básico con `-sV -T4 -Pn`
- [x] Generación de informe Markdown
- [x] Ejemplo de informe real incluido
- [ ] Soporte para múltiples perfiles (Quick / Top1000 / Full)
- [ ] Exportación a PDF
- [ ] Integración con Wazuh para alertas automáticas
- [ ] Modo batch (múltiples targets desde fichero)

---

## 👤 Autor

**Nacho Menárguez** — [ai.menarguez-ia.com](https://ai.menarguez-ia.com) · [LinkedIn](https://www.linkedin.com/in/ignaciomenarguezfernandez/)

---

<div align="center">
<sub>⚡ Parte del ecosistema Menárguez-IA · Blue Team & SOC Automation · 2026</sub>
</div>
