# 🔍 Informe de Reconocimiento Nmap
## Target: menarguez-ia.com

---

```
Menarguez-IA Solutions · SOC Report
Generado automáticamente por nmap-auto-reporter
Herramienta: https://github.com/Nachomf112/nmap-auto-reporter
```

---

## 📋 Metadatos del escaneo

| Campo | Valor |
|-------|-------|
| **Target** | menarguez-ia.com |
| **IP resuelta** | 185.230.63.107 |
| **Fecha** | 2025-05-07 09:14:32 UTC |
| **Duración** | 12.43 segundos |
| **Tipo de escaneo** | SYN Stealth + Version Detection + Default Scripts |
| **Comando ejecutado** | `nmap -sV -sC -T4 -oX output.xml menarguez-ia.com` |
| **Versión Nmap** | 7.94 |
| **Usuario** | nacho@menarguez-soc |

---

## 🌐 Información del host

| Campo | Valor |
|-------|-------|
| **Hostname** | menarguez-ia.com |
| **IP** | 185.230.63.107 |
| **Estado** | 🟢 UP |
| **Latencia** | 18ms |
| **OS detectado** | Linux (kernel 5.x) — confianza 85% |
| **TTL** | 54 |

---

## 🔓 Puertos abiertos detectados

| Puerto | Estado | Servicio | Versión | Observación |
|--------|--------|---------|---------|-------------|
| **80/tcp** | 🟢 open | http | nginx 1.24.0 | Redirige a HTTPS |
| **443/tcp** | 🟢 open | https | nginx 1.24.0 | SSL/TLS activo |
| **22/tcp** | 🔴 filtered | ssh | — | Filtrado por firewall |
| **8080/tcp** | 🔴 closed | http-alt | — | Cerrado |
| **3306/tcp** | 🔴 closed | mysql | — | Cerrado |

**Resumen:** 2 puertos abiertos · 1 filtrado · 2 cerrados

---

## 🔐 Análisis SSL/TLS (puerto 443)

```
ssl-cert:
  Subject: commonName=menarguez-ia.com
  Subject Alternative Names: menarguez-ia.com, www.menarguez-ia.com
  Issuer: Let's Encrypt Authority X3
  Valid from: 2025-03-01
  Valid until: 2025-06-01
  Bits: 2048 RSA
  SHA-256: a3:f2:91:bc:44:d1:...

ssl-enum-ciphers:
  TLSv1.2:
    ciphers:
      TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 - A
      TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 - A
  TLSv1.3:
    ciphers:
      TLS_AKE_WITH_AES_256_GCM_SHA384 - A
  least strength: A
```

**✅ Resultado SSL:** Configuración segura. TLS 1.2 y 1.3. Sin ciphers débiles detectados.

---

## 📜 Scripts NSE ejecutados

### http-title (puerto 80/443)
```
80/tcp  → "301 Moved Permanently"
443/tcp → "Menarguez-IA Solutions · Automatización con IA"
```

### http-server-header
```
Server: nginx/1.24.0
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=31536000
```

### http-robots
```
/wp-admin/
/wp-login.php
/xmlrpc.php
```
⚠️ **Observación:** Rutas WordPress expuestas en robots.txt. Recomendable revisar si el panel admin está correctamente protegido.

### http-methods
```
Métodos permitidos: GET, POST, HEAD, OPTIONS
PUT/DELETE: NO permitidos ✅
TRACE: NO permitido ✅
```

---

## ⚠️ Hallazgos y observaciones

### 🔴 Crítico
> Ninguno detectado.

### 🟠 Alto
> Ninguno detectado.

### 🟡 Medio

| ID | Hallazgo | Detalle |
|----|---------|---------|
| M-01 | Rutas WordPress en robots.txt | `/wp-admin/` y `/wp-login.php` visibles públicamente. Aunque no implica vulnerabilidad directa, facilita reconocimiento. |

### 🟢 Bajo / Informativo

| ID | Hallazgo | Detalle |
|----|---------|---------|
| I-01 | Versión nginx expuesta | `nginx/1.24.0` visible en headers. Recomendable ocultar con `server_tokens off`. |
| I-02 | Certificado SSL próximo a expirar | Válido hasta 2025-06-01. Let's Encrypt renueva automáticamente si está configurado. Verificar renovación automática activa. |

---

## ✅ Buenas prácticas confirmadas

| Control | Estado |
|---------|--------|
| HTTPS activo y forzado | ✅ |
| HSTS configurado | ✅ |
| TLS 1.3 habilitado | ✅ |
| Ciphers débiles (RC4, DES) | ✅ No detectados |
| Métodos peligrosos (PUT, TRACE) | ✅ Deshabilitados |
| Puerto SSH (22) expuesto | ✅ Filtrado |
| X-Frame-Options | ✅ Configurado |
| X-Content-Type-Options | ✅ Configurado |

---

## 📊 Puntuación de superficie de ataque

```
┌─────────────────────────────────────────┐
│  Superficie de ataque externa           │
│                                         │
│  Puertos expuestos:    ██░░░░░░░░  2/10 │
│  Configuración SSL:    ████████░░  8/10 │
│  Headers seguridad:    ███████░░░  7/10 │
│  Info. sensible:       █░░░░░░░░░  1/10 │
│                                         │
│  PUNTUACIÓN GLOBAL:    7.8 / 10  🟢     │
└─────────────────────────────────────────┘
```

---

## 🛠️ Recomendaciones

### Prioritarias

1. **Ocultar versión de nginx** — Añadir `server_tokens off;` en `/etc/nginx/nginx.conf`
2. **Revisar exposición rutas WordPress** — Evaluar si el acceso a `/wp-admin/` está protegido con IP allowlist o 2FA
3. **Verificar renovación automática SSL** — Ejecutar `certbot renew --dry-run` para confirmar que Let's Encrypt renueva automáticamente

### Opcionales

4. **Añadir Content-Security-Policy (CSP)** — Header adicional de seguridad no detectado
5. **Añadir Permissions-Policy** — Control de permisos del navegador

---

## 📁 Archivos generados

```
reports/
├── ejemplo_scan_menarguez-ia.md     ← este informe
├── ejemplo_scan_menarguez-ia.xml    ← output raw Nmap
└── ejemplo_scan_menarguez-ia.json   ← datos estructurados
```

---

## 🔗 Referencias

- [Nmap Reference Guide](https://nmap.org/book/man.html)
- [OWASP Testing Guide - Network](https://owasp.org/www-project-web-security-testing-guide/)
- [MITRE ATT&CK T1046 - Network Service Discovery](https://attack.mitre.org/techniques/T1046/)

---

```
─────────────────────────────────────────────────────
Generado por nmap-auto-reporter · Menarguez-IA Solutions
github.com/Nachomf112/nmap-auto-reporter
ai.menarguez-ia.com · Ignacio Menárguez Fernández
─────────────────────────────────────────────────────
[+] Informe listo para adjuntar al ticket del SOC o informe.
```
