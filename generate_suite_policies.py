#!/usr/bin/env python3
"""Generate four offline-app privacy policy pages for PocketMind Suite."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EFFECTIVE = "September 12, 2026"
UPDATED = "September 12, 2026"
DEV = "Muhammad Nouman Shakeel / PocketMind"
COUNTRY = "Pakistan"
CONTACT_WA = "https://wa.me/923405055603?text=Hi%20Nouman%2C%20I%20have%20a%20question%20about%20PocketMind%20privacy."
HOME = "./index.html"

CSS = r"""
:root{
  --bg:#050810;--bg2:#080c18;--surface:rgba(255,255,255,0.03);
  --border:rgba(255,255,255,0.07);--border-bright:rgba(99,179,255,0.3);
  --cyan:#63B3FF;--cyan-dim:rgba(99,179,255,0.15);
  --text:#E8EDF5;--text-muted:rgba(232,237,245,0.5);
  --font-head:'Syne',sans-serif;--font-serif:'Instrument Serif',serif;--font-mono:'JetBrains Mono',monospace;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:var(--font-head);line-height:1.6;min-height:100vh;}
a{color:var(--cyan);text-decoration:none;}
a:hover{text-decoration:underline;}
.wrap{max-width:920px;margin:0 auto;padding:40px 20px 80px;}
.topbar{display:flex;gap:12px;flex-wrap:wrap;margin-bottom:28px;}
.btn{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--text);font-size:.88rem;}
.btn-primary{border-color:var(--border-bright);background:var(--cyan-dim);color:var(--cyan);}
.policy-card{background:linear-gradient(135deg,rgba(255,255,255,.045),rgba(255,255,255,.018));border:1px solid var(--border);border-radius:24px;padding:34px;box-shadow:0 18px 80px rgba(0,0,0,.22);}
.pm-kicker{font-family:var(--font-mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--cyan);margin-bottom:10px;}
.policy-card h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.05;letter-spacing:-.04em;margin-bottom:12px;}
.policy-card h1 em{font-family:var(--font-serif);color:var(--cyan);font-weight:400;}
.policy-meta{font-family:var(--font-mono);font-size:.78rem;color:var(--cyan);letter-spacing:.06em;text-transform:uppercase;margin-bottom:28px;}
.policy-card h2{font-size:1.2rem;margin:28px 0 10px;}
.policy-card p,.policy-card li{color:var(--text-muted);font-size:.95rem;line-height:1.8;}
.policy-card ul{padding-left:22px;margin:10px 0 16px;}
.policy-callout{border:1px solid var(--border-bright);background:var(--cyan-dim);border-radius:18px;padding:18px;margin:22px 0;color:var(--text);}
.policy-callout strong{color:var(--cyan);}
.policy-actions{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px;padding-top:24px;border-top:1px solid var(--border);}
.app-links{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin:18px 0 8px;}
.app-links a{display:block;padding:12px 14px;border-radius:14px;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);font-size:.85rem;}
.app-links a.active{border-color:var(--border-bright);color:var(--cyan);}
"""

APPS = [
    {
        "slug": "localchat",
        "file": "privacy-localchat.html",
        "title": "PocketMind Local Chat",
        "em": "Local Chat",
        "package": "com.pocketmind.localchat",
        "one_liner": "an offline-only Android chat app that runs local GGUF language models on your device (including optional Vulkan/GPU acceleration where supported)",
        "summary": "PocketMind Local Chat is a paid, offline-first chat app. Prompts, chat history, and model inference stay on your phone. There is no PocketMind cloud inbox, no freemium quotas, and no in-app online AI providers.",
        "stores_local": [
            "Chat messages and session history you create in the App",
            "App settings (appearance/theme, font, Vulkan/GPU layer preferences where available)",
            "Imported or selected offline GGUF model files stored in app storage",
            "Temporary working files created during local inference",
        ],
        "processing": [
            "When you chat with a loaded local model, prompts and responses are processed on-device using the bundled local runtime (for example llama.cpp with CPU and optional Vulkan).",
            "The App does not include online chat providers, organization-server mode, or BYOK cloud APIs.",
            "Internet connectivity is not required for core chat once a model file is on your device. Google Play may still process purchase/restore activity under Google’s policies.",
        ],
        "permissions": [
            "Storage / document access via Android system pickers when you import a model file",
            "Optional GPU/Vulkan hardware features when available (not required to install)",
            "No microphone permission is required for core Local Chat use",
        ],
        "extra_sections": "",
    },
    {
        "slug": "imagelab",
        "file": "privacy-imagelab.html",
        "title": "PocketMind Image Lab",
        "em": "Image Lab",
        "package": "com.pocketmind.imagelab",
        "one_liner": "an offline Android image-generation studio that runs local Stable Diffusion–style models on your device (GPU/Vulkan when available, otherwise CPU)",
        "summary": "PocketMind Image Lab is a paid, offline image app. Prompts, model files, and generated images are handled on-device. There is no PocketMind cloud gallery and no online image-provider mode in this App.",
        "stores_local": [
            "Text prompts and negative prompts you enter",
            "Imported offline image model files (for example safetensors) in app storage",
            "Generated images you keep in the App session/storage",
            "App settings (appearance/theme, font, and related preferences)",
            "Temporary working files created during generation",
        ],
        "processing": [
            "Image generation runs locally using the on-device image runtime. Prompts are not sent to PocketMind servers.",
            "This App does not ship online Image Studio providers. Core generation does not require contacting third-party AI APIs.",
            "Google Play may process purchase/restore activity under Google’s policies.",
        ],
        "permissions": [
            "Storage / document access via Android system pickers when you import a model",
            "Optional GPU/Vulkan hardware features when available",
            "No camera permission is required for core generation from text prompts",
        ],
        "extra_sections": """
    <h2>6. Generated images</h2>
    <p>Generated images may depict people, brands, or other content depending on your prompt and model. You are responsible for lawful use of outputs and for respecting third-party rights. Images remain on your device unless you export or share them yourself.</p>
""",
    },
    {
        "slug": "voicelab",
        "file": "privacy-voicelab.html",
        "title": "PocketMind Voice Lab",
        "em": "Voice Lab",
        "package": "com.pocketmind.voicelab",
        "one_liner": "an offline Android voice studio for on-device speech generation and cloning-style workflows using device/local speech paths (including Android system text-to-speech where used)",
        "summary": "PocketMind Voice Lab is a paid, offline voice app. Text you enter, reference audio you select, and synthesized audio stay on your device for the on-device path. This App does not include online voice providers such as ElevenLabs or OpenAI Audio.",
        "stores_local": [
            "Text prompts you enter for speech generation",
            "Reference audio files you import for cloning-style workflows (if used)",
            "Generated / synthesized audio files written to app storage",
            "App settings (appearance/theme, font, and related preferences)",
            "Temporary working files created during synthesis",
        ],
        "processing": [
            "Speech synthesis is performed on-device (for example via Android System Text-to-Speech and/or other local engines exposed in the App). PocketMind does not operate a cloud voice API for this App.",
            "Status shown in the App is intended to reflect real on-device capability (CPU / system TTS). Do not assume a separate PocketMind cloud GPU voice backend.",
            "Google Play may process purchase/restore activity under Google’s policies.",
        ],
        "permissions": [
            "Microphone / record audio if you capture reference speech on device (only when that flow is used)",
            "Storage / document / audio pickers when you import reference files",
            "No online voice-provider account is required for core offline use",
        ],
        "extra_sections": """
    <h2>6. Voice cloning sensitivity</h2>
    <p><strong>High-risk disclosure:</strong> Reference audio and cloned-style outputs can be biometric or otherwise sensitive. If you use another person’s voice, you must have all rights and consents required by law. Do not use Voice Lab to impersonate someone without authorization, to commit fraud, or to violate platform rules. Because this App’s core path is on-device, PocketMind does not receive your reference audio on PocketMind servers; keep device access and exports under your control.</p>
""",
    },
    {
        "slug": "characters",
        "file": "privacy-characters.html",
        "title": "PocketMind Characters",
        "em": "Characters",
        "package": "com.pocketmind.characters",
        "one_liner": "an offline Android app for creating character personas and chatting with them using local GGUF models that fit available device RAM",
        "summary": "PocketMind Characters is a paid, offline persona + chat app. Character definitions, chat content, and model inference stay on your phone. Model selection is gated by free RAM checks performed on-device. There is no PocketMind cloud character sync.",
        "stores_local": [
            "Character names and system/persona prompts you create",
            "Chat messages exchanged with a selected character",
            "Imported offline GGUF model files in app storage",
            "App settings (appearance/theme, font, Vulkan/GPU layer preferences where available)",
            "Temporary working files created during local inference",
        ],
        "processing": [
            "Character CRUD and chat run locally. Persona prompts are combined with your messages and processed by the loaded on-device model.",
            "Before loading a model, the App may estimate whether the file size fits available free RAM (plus headroom). That check uses on-device memory information and does not upload the model to PocketMind.",
            "The App does not include online chat providers or organization-server mode.",
            "Google Play may process purchase/restore activity under Google’s policies.",
        ],
        "permissions": [
            "Storage / document access via Android system pickers when you import a model file",
            "Optional GPU/Vulkan hardware features when available",
            "No account login is required to create or chat with characters",
        ],
        "extra_sections": """
    <h2>6. Personas and sensitive prompts</h2>
    <p>Character prompts and chats may contain personal or sensitive text you choose to write. Because content stays on-device, protect your phone with a lock screen and be careful with Android backups/exports that may copy app data.</p>
""",
    },
]


def bullets(items):
    return "\n".join(f"      <li>{x}</li>" for x in items)


def page(app, all_apps):
    links = []
    for a in all_apps:
        cls = "active" if a["slug"] == app["slug"] else ""
        links.append(f'<a class="{cls}" href="./{a["file"]}">{a["title"]}</a>')
    link_grid = "\n      ".join(links)

    extra_num_offset = 0
    # sections 1-5 standard, extra may add 6, then continue numbering
    has_extra = bool(app["extra_sections"].strip())
    next_n = 7 if has_extra else 6

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{app["title"]} — Privacy Policy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
  <div class="wrap">
    <div class="topbar">
      <a class="btn" href="{HOME}">← Portfolio</a>
      <a class="btn btn-primary" href="{HOME}#privacy-policy">Hybrid AI policy</a>
    </div>
    <div class="app-links">
      {link_grid}
    </div>
    <div class="policy-card">
      <div class="pm-kicker">Public Privacy Policy · Google Play</div>
      <h1>PocketMind <em>{app["em"]}</em></h1>
      <div class="policy-meta">Effective Date: {EFFECTIVE} · Last Updated: {UPDATED} · Developer: {DEV} · Country: {COUNTRY}</div>

      <p>This Privacy Policy describes how <strong>{app["title"]}</strong> for Android (“the App,” “we,” “our,” or “us”) handles information when you install and use the App. The App is {app["one_liner"]}.</p>
      <p>Google Play application id: <strong>{app["package"]}</strong>.</p>
      <p>By downloading, installing, or using the App, you acknowledge that you have read this Privacy Policy. If you do not agree, do not use the App.</p>

      <div class="policy-callout"><strong>Plain-language summary:</strong> {app["summary"]} Purchases (if any) are processed by Google Play under Google’s policies. We do not sell your personal content for advertising.</div>

      <h2>1. Scope and roles</h2>
      <p><strong>1.1 What this policy covers.</strong> This policy covers the Android application <strong>{app["title"]}</strong> ({app["package"]}) distributed through Google Play and the on-device features described below.</p>
      <p><strong>1.2 Related PocketMind apps.</strong> PocketMind also publishes other apps (including PocketMind Hybrid AI and the other offline suite apps). Each app has its own privacy policy URL. This document applies only to <strong>{app["title"]}</strong>.</p>
      <p><strong>1.3 Controller / developer.</strong> The developer is {DEV}, {COUNTRY}. For purchase processing, Google LLC / Google Play acts as payment processor under Google’s Privacy Policy and Google Play Terms.</p>
      <p><strong>1.4 What this policy does not cover.</strong> This policy does not govern third-party websites, model hosts, Android system services, device manufacturer backups, or Google Play beyond what is stated here.</p>

      <h2>2. Information we do not collect on PocketMind-operated servers</h2>
      <p>PocketMind does not currently operate a developer-owned backend that creates user accounts for this App, hosts your private content in a PocketMind cloud inbox, or sells your conversations/images/audio to advertisers.</p>
      <p>In particular, we do not intentionally:</p>
      <ul>
        <li>Sell your personal data or private app content;</li>
        <li>Use your private content to build advertising profiles for third-party ads in the App;</li>
        <li>Require a PocketMind cloud login to use core features;</li>
        <li>Upload your local models or chats to a PocketMind-owned server as part of normal App operation.</li>
      </ul>
      <p><strong>Important limitation:</strong> “We do not collect on PocketMind servers” does not mean “nothing ever touches another company.” Google Play (purchases), Android system services (for example system TTS), and device/cloud backups you enable may process technical or purchase-related data under their own policies.</p>

      <h2>3. Information stored locally on your device</h2>
      <p>Depending on how you use the App, it may store information in on-device app storage (and related Android storage you authorize), including:</p>
      <ul>
{bullets(app["stores_local"])}
      </ul>
      <p>Local storage remains on your device until you delete it, clear app data, uninstall the App, or otherwise remove those files. Device backups (Android backup / manufacturer cloud backup), if enabled, may copy app data off-device under those systems’ rules.</p>

      <h2>4. Paid app and Google Play</h2>
      <p>{app["title"]} is distributed as a <strong>paid one-time Google Play application</strong> (not a freemium product with in-app Pro quotas). There are no separate in-app subscription gates inside the App for core features described here.</p>
      <p>Payment, refunds, order history, and purchase identity are handled by Google Play. PocketMind does not receive your full payment card details. Google may process purchase tokens, product identifiers, order data, and account/device information necessary to complete or restore the purchase.</p>

      <h2>5. On-device processing</h2>
      <ul>
{bullets(app["processing"])}
      </ul>
{app["extra_sections"]}
      <h2>{next_n}. Permissions</h2>
      <p>Depending on Android version and the feature you use, the App may request or use:</p>
      <ul>
{bullets(app["permissions"])}
      </ul>
      <p>You can deny non-essential permissions; related features may then be unavailable.</p>

      <h2>{next_n + 1}. Analytics, advertising, and tracking</h2>
      <p>The App is designed around on-device AI functionality. It does not currently integrate a separate third-party advertising SDK for the purpose of selling your content to advertisers, and PocketMind does not currently operate PocketMind-owned product-analytics servers that ingest your private prompts or outputs from this App.</p>
      <p>Android, Google Play, and crash/diagnostics facilities you enable at the OS level may still collect technical data independently under their policies.</p>

      <h2>{next_n + 2}. Data sharing</h2>
      <p>We do not sell your personal data. Information may leave your device when:</p>
      <ul>
        <li>You purchase or restore the App through Google Play;</li>
        <li>You export, share, or back up files yourself;</li>
        <li>Android system services you invoke (for example system TTS engines) process text/audio locally or according to that engine’s vendor behavior;</li>
        <li>Disclosure is required by law, lawful government request, or to protect rights, safety, and security where legally permitted.</li>
      </ul>

      <h2>{next_n + 3}. Retention and deletion</h2>
      <p><strong>On device:</strong> Local data remains until you delete content in the App, clear app storage, or uninstall. Uninstalling removes app-private storage but does not erase files you previously exported to shared storage, nor Google Play purchase records.</p>
      <p><strong>With Google / Android:</strong> Retention of purchase and platform data is controlled by Google and your device vendor. Use Google Play / Android settings tools for those systems.</p>

      <h2>{next_n + 4}. Children’s privacy</h2>
      <p>The App is not directed to children under 13 (or the minimum age required in your country). Do not use the App if you are under the applicable age. We do not knowingly collect personal information from children on PocketMind servers.</p>

      <h2>{next_n + 5}. International users</h2>
      <p>The developer is based in Pakistan. If you use the App from another country, your local data remains on your device, while Google Play and Android platform services may process data in other regions under their policies.</p>

      <h2>{next_n + 6}. Changes to this policy</h2>
      <p>We may update this Privacy Policy to reflect product or legal changes. The “Last Updated” date at the top will change when we do. Continued use of the App after an update means you acknowledge the revised policy. Material changes may also be noted on this page.</p>

      <h2>{next_n + 7}. Contact</h2>
      <p>Questions about this Privacy Policy or {app["title"]}:</p>
      <p><strong>Muhammad Nouman Shakeel / PocketMind</strong><br>Pakistan<br>WhatsApp: +92 340 5055603</p>
      <p>Please do not send passwords or sensitive credentials over unsecured channels.</p>

      <div class="policy-actions">
        <a href="{HOME}" class="btn">Back to Portfolio</a>
        <a href="{CONTACT_WA}" target="_blank" rel="noopener" class="btn btn-primary">Contact Me →</a>
      </div>
    </div>
  </div>
</body>
</html>
"""


def main():
    for app in APPS:
        path = ROOT / app["file"]
        path.write_text(page(app, APPS), encoding="utf-8")
        print("wrote", path.name)

    # Patch index.html: add suite policy links near privacy summary / full policy
    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    marker = "Open Full Privacy Policy →</a>"
    suite_block = """Open Full Privacy Policy →</a>
      <div class="app-links" style="margin-top:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:10px;">
        <a href="./privacy-localchat.html" style="display:block;padding:12px 14px;border-radius:14px;border:1px solid rgba(255,255,255,0.07);background:rgba(255,255,255,0.03);color:rgba(232,237,245,0.5);font-size:.85rem;">Local Chat policy</a>
        <a href="./privacy-imagelab.html" style="display:block;padding:12px 14px;border-radius:14px;border:1px solid rgba(255,255,255,0.07);background:rgba(255,255,255,0.03);color:rgba(232,237,245,0.5);font-size:.85rem;">Image Lab policy</a>
        <a href="./privacy-voicelab.html" style="display:block;padding:12px 14px;border-radius:14px;border:1px solid rgba(255,255,255,0.07);background:rgba(255,255,255,0.03);color:rgba(232,237,245,0.5);font-size:.85rem;">Voice Lab policy</a>
        <a href="./privacy-characters.html" style="display:block;padding:12px 14px;border-radius:14px;border:1px solid rgba(255,255,255,0.07);background:rgba(255,255,255,0.03);color:rgba(232,237,245,0.5);font-size:.85rem;">Characters policy</a>
      </div>"""
    if "privacy-localchat.html" not in html:
        if marker not in html:
            raise SystemExit("Could not find privacy link marker in index.html")
        html = html.replace(marker, suite_block, 1)
        index.write_text(html, encoding="utf-8")
        print("patched index.html with suite policy links")
    else:
        print("index.html already has suite links")


if __name__ == "__main__":
    main()
