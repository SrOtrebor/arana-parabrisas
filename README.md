# Parabrisas Arana — Landing Page

> Landing page institucional de alta conversión para campaña de Meta Ads.  
> Empresa especializada en parabrisas y cristales para camiones, flotas y transporte — **Zona Oeste, Gran Buenos Aires**.

🌐 **Sitio en vivo:** [https://srotrebor.github.io/arana-parabrisas/](https://srotrebor.github.io/arana-parabrisas/)

---

## Índice

1. [Descripción del proyecto](#descripción-del-proyecto)
2. [Tecnologías utilizadas](#tecnologías-utilizadas)
3. [Estructura del proyecto](#estructura-del-proyecto)
4. [Secciones del sitio](#secciones-del-sitio)
5. [Optimización SEO y Geo](#optimización-seo-y-geo)
6. [Optimización AEO (búsquedas por IA)](#optimización-aeo-búsquedas-por-ia)
7. [Seguridad implementada](#seguridad-implementada)
8. [Guía de mantenimiento](#guía-de-mantenimiento)
9. [Despliegue](#despliegue)
10. [Créditos](#créditos)

---

## Descripción del proyecto

Sitio web estático de una sola página (`index.html`) diseñado como landing page de conversión para soportar una campaña agresiva de publicidad en Meta Ads (Facebook/Instagram). El objetivo principal es convertir el tráfico pagado en consultas por WhatsApp.

### Características principales

- ✅ **Diseño 100% responsivo** — Mobile-first, optimizado para tráfico desde celulares
- ✅ **Solución llave en mano** — Un único archivo HTML con CSS y JS embebidos
- ✅ **Alta conversión (CRO)** — Múltiples CTAs de WhatsApp en puntos estratégicos
- ✅ **SEO local avanzado** — Optimizado para Zona Oeste GBA
- ✅ **AEO completo** — Visible para ChatGPT, Perplexity, Google AI Overview y Gemini
- ✅ **Auditoría de seguridad aprobada** — 11 de 12 hallazgos resueltos
- ✅ **Sin dependencias externas** — Fuentes e imágenes autoalojadas en el repo

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| HTML5 semántico | Estructura de la página |
| CSS3 vanilla | Estilos, animaciones, diseño responsivo |
| JavaScript vanilla | Menú mobile, acordeón FAQ, animaciones de scroll |
| Schema.org JSON-LD | Datos estructurados para SEO y AEO |
| GitHub Pages | Hosting gratuito con HTTPS |
| Poppins (local) | Tipografía — autoalojada en `/assets/fonts/` |

> No se utilizan frameworks externos (sin React, sin Vue, sin Bootstrap, sin jQuery). El sitio carga en menos de 2 segundos desde el servidor de GitHub Pages.

---

## Estructura del proyecto

```
arana-parabrisas/
│
├── index.html              # Toda la landing page (HTML + CSS + JS en un solo archivo)
├── sitemap.xml             # Mapa del sitio para indexación en buscadores e IA
├── robots.txt              # Permisos para rastreadores, incluidos bots de IA
│
├── assets/
│   ├── logo.png                # Logo oficial Arana (fondo transparente)
│   ├── logo-letra-negra.png    # Logo con texto en negro (para fondos blancos)
│   ├── hero-bg.jpg             # Imagen de fondo del hero (camión en ruta)
│   ├── nosotros.png            # Imagen sección Quiénes Somos (generada con IA)
│   ├── instalacion.jpg         # Imagen de respaldo (no utilizada actualmente)
│   └── fonts/
│       ├── Poppins-Regular.ttf
│       ├── Poppins-Medium.ttf
│       ├── Poppins-SemiBold.ttf
│       ├── Poppins-Bold.ttf
│       ├── Poppins-BoldItalic.ttf
│       ├── Poppins-ExtraBold.ttf
│       ├── Poppins-Black.ttf
│       └── Poppins-BlackItalic.ttf
│
└── Contexto/               # Material de marca original (no se publica en el sitio)
    ├── Estrategia de Marca - Parabrisas Arana.pdf
    ├── Font-*/             # Fuentes Poppins originales y logos
    └── WhatsApp Image *.jpeg   # Fotos de referencia de las sucursales
```

---

## Secciones del sitio

| # | ID | Nombre | Propósito CRO |
|---|---|---|---|
| 1 | `#urgency-banner` | Banner de urgencia | Franja roja fija con oferta de servicio a domicilio sin cargo |
| 2 | `#navbar` | Navegación | Logo + links internos + botón WhatsApp siempre visible |
| 3 | `#hero` | Hero / Inicio | H1 de impacto + CTA principal + 4 badges de confianza |
| 4 | `#pain` | Pain Points | Activa el dolor del usuario antes de ofrecer la solución |
| 5 | `#nosotros` | Quiénes Somos | 50 años, 3 sucursales, estadísticas, badge Pilkington |
| 6 | `#servicios` | Servicios | 6 tarjetas de servicios con hover effect |
| 7 | `#empresas` | Empresas de Transporte | Sección B2B oscura de alto impacto para flotas |
| 8 | `#particulares` | Particulares | Sección B2C con proceso de 3 pasos |
| 9 | `#faq` | Preguntas Frecuentes | Acordeón con 8 preguntas + doble función SEO/AEO |
| 10 | `#confianza` | Por qué elegirnos | Pilkington, garantía, técnicos certificados |
| 11 | `#sucursales` | Dónde estamos | 3 cards con dirección, teléfono y link a Google Maps |
| 12 | `#cta-final` | CTA Final | Cierre agresivo con botón grande de WhatsApp |
| — | Flotante | Botón WhatsApp sticky | Desktop: círculo pulsante. Mobile: barra fija al pie |

---

## Optimización SEO y Geo

### Meta tags primarios
- **Título**: incluye las 3 ciudades principales (Paso del Rey, Merlo, González Catán)
- **Descripción**: 160 caracteres con keywords del rubro + localización
- **Keywords**: 12 términos clave del sector transporte en Zona Oeste
- **Canonical**: apunta a la URL de GitHub Pages
- **robots**: `index, follow`

### Geo targeting
```html
<meta name="geo.region" content="AR-B" />
<meta name="geo.placename" content="Zona Oeste, Gran Buenos Aires" />
<meta name="geo.position" content="-34.6385;-58.7768" />
<meta name="ICBM" content="-34.6385, -58.7768" />
```

### Open Graph (Meta Ads)
- Tipo: `business.business`
- Título pensado para capturar dolor: *"¿Tu flota está parada por un parabrisas roto?"*
- Imagen OG: logo con texto
- Datos de contacto y dirección de la sucursal principal

### Schema.org JSON-LD (3 bloques)

| Schema | Tipo | Contenido |
|---|---|---|
| LocalBusiness | `AutoRepair` | Empresa completa con las 3 sucursales, coordenadas, horarios |
| FAQPage | `FAQPage` | 10 preguntas y respuestas estructuradas |
| HowTo | `HowTo` | Proceso de 3 pasos para contratar el servicio |

---

## Optimización AEO (búsquedas por IA)

El sitio está optimizado para aparecer en respuestas generadas por:
- **ChatGPT** (OpenAI) — via GPTBot
- **Perplexity** — via PerplexityBot
- **Google AI Overview / Gemini** — via Google-Extended
- **Bing Copilot** — via Bingbot
- **Claude** (Anthropic) — via anthropic-ai / Claude-Web

### Estrategia implementada

1. **FAQ Schema**: 10 preguntas del rubro respondidas directamente en formato `Question`/`Answer`
2. **HowTo Schema**: Proceso de contratación en formato `HowToStep`
3. **Sección FAQ visible**: El texto de las respuestas también está en el HTML plano, legible por cualquier rastreador
4. **robots.txt explícito**: Autoriza individualmente a cada bot de IA conocido
5. **sitemap.xml**: Las 7 secciones principales del sitio indexadas con prioridad

### Ejemplo de pregunta capturada
> *"¿Dónde puedo cambiar el parabrisas de mi camión en la Zona Oeste?"*  
> → El sitio responde con dirección, teléfono y horario de las 3 sucursales en formato estructurado.

---

## Seguridad implementada

Auditoría realizada el 28/05/2025. 11 de 12 hallazgos resueltos.

### Headers de seguridad activos (via meta http-equiv)

| Header | Valor | Protege contra |
|---|---|---|
| `Content-Security-Policy` | `default-src 'self'` + reglas específicas | Inyección de scripts, clickjacking, objetos embebidos |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | Fuga de URL de campaña a terceros |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=()` | Acceso no autorizado a APIs del navegador |
| `X-Content-Type-Options` | `nosniff` | MIME sniffing |
| `frame-ancestors 'none'` | (dentro de CSP) | Clickjacking vía iframe |

### Otras medidas

- ✅ **HTTPS forzado** por GitHub Pages
- ✅ **`rel="noopener noreferrer"`** en los 14 links externos (WhatsApp, Maps, Instagram, Estudio Precinto)
- ✅ **Sin event handlers inline** (`onmouseover`, `onclick`, etc.) — todo en CSS/JS separado
- ✅ **Fuentes autoalojadas** — sin dependencia de Google Fonts (privacidad del usuario)
- ✅ **Imágenes autoalojadas** — sin dependencia de CDN de terceros (Unsplash)
- ⬜ **Ofuscación de teléfono** — opcional, no implementada (es página de contacto)

---

## Guía de mantenimiento

### Cambiar el número de WhatsApp

El número actual es `+54 9 11 6383-0297`. Aparece en el código como `5491163830297` (formato internacional sin espacios ni signos).

Para cambiarlo, buscar `5491163830297` en `index.html` y reemplazarlo en todas sus ocurrencias (aparece 9 veces).

### Cambiar las direcciones de las sucursales

Buscar en `index.html` los comentarios `<!-- SUCURSAL -->` o los textos:
- `Bartolomé Mitre 1409` → Paso del Rey
- `Juan Manuel de Rosas 18178` → González Catán
- `Av. Ricardo Balbín 3803` → Merlo

### Cambiar los links de Google Maps

Buscar `google.com/maps` en `index.html`. Hay 3 links, uno por sucursal. Reemplazarlos con los links "Cómo llegar" de Google Maps reales.

### Actualizar el logo

Reemplazar los archivos en `assets/`:
- `logo.png` → versión con fondo transparente (para navbar oscura)
- `logo-letra-negra.png` → versión con texto negro (para Open Graph)

### Publicar cambios

```bash
git add -A
git commit -m "descripción del cambio"
git push origin main
```

GitHub Pages actualiza el sitio automáticamente en 1-3 minutos.

---

## Despliegue

El sitio está desplegado en **GitHub Pages** de forma gratuita.

- **URL:** `https://srotrebor.github.io/arana-parabrisas/`
- **Rama activa:** `main`
- **Carpeta raíz:** `/` (raíz del repositorio)
- **HTTPS:** Activado automáticamente por GitHub

### Activar GitHub Pages (si se clona el repo)

1. Ir a **Settings** del repositorio en GitHub
2. Sección **Pages** en el menú izquierdo
3. Branch: `main` / Folder: `/ (root)`
4. Hacer clic en **Save**
5. Esperar 2-3 minutos

---

## Créditos

| Rol | Responsable |
|---|---|
| Desarrollo web, SEO, AEO y seguridad | [Estudio Precinto](https://estudioprecinto.com) |
| Imagen sección "Quiénes Somos" | Generada con IA (Antigravity / Google DeepMind) |
| Tipografía | Poppins — Google Fonts (OFL License) |
| Marca y contenido | Parabrisas Arana |

---

*Última actualización: Mayo 2025*
