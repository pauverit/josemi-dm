import base64
import os

logo_html = '<div style="font-weight: 900; font-size: 24px; letter-spacing: -1px;">DIGITAL <span style="color:var(--accent-1)">MARKET</span></div>'
logo_path = 'logo-dm.png'

if os.path.exists(logo_path):
    with open(logo_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        logo_html = f'<img src="data:image/png;base64,{encoded_string}" alt="Digital Market Logo" style="height: 50px; width: auto;">'

html_content = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Market — Centro de Herramientas</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-primary: #ffffff;
            --accent-1: #0088cc;
            --accent-dark: #006699;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --gray-light: #f1f5f9;
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }}

        .bg-decor {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1; pointer-events: none;
            background: radial-gradient(circle at 80% 20%, #e0f2fe 0%, transparent 40%),
                        radial-gradient(circle at 10% 80%, #f1f5f9 0%, transparent 30%);
        }}

        header {{
            padding: 30px 24px;
            max-width: 1200px; margin: 0 auto;
            width: 100%;
            display: flex; justify-content: space-between; align-items: center;
        }}

        .hero {{
            text-align: center;
            padding: 60px 24px 30px;
            max-width: 800px;
            margin: 0 auto;
        }}
        .hero h1 {{
            font-size: 56px; font-weight: 900; line-height: 1.1;
            margin-bottom: 20px; letter-spacing: -2px;
        }}
        .hero h1 span {{ color: var(--accent-1); }}
        .hero p {{
            font-size: 20px; color: var(--text-secondary);
            font-weight: 400; max-width: 600px; margin: 0 auto;
        }}

        .cards-container {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 30px;
            max-width: 1100px;
            margin: 40px auto;
            padding: 0 24px 100px;
            width: 100%;
        }}

        .card {{
            background: #fff;
            border-radius: 32px;
            padding: 50px;
            text-decoration: none;
            color: inherit;
            border: 2px solid var(--gray-light);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        }}
        .card:hover {{
            transform: translateY(-10px);
            border-color: var(--accent-1);
            box-shadow: 0 30px 60px rgba(0,136,204,0.1);
        }}

        .card-icon {{
            font-size: 48px;
            margin-bottom: 24px;
            background: var(--gray-light);
            width: 80px; height: 80px;
            border-radius: 24px;
            display: flex; align-items: center; justify-content: center;
            transition: all 0.3s;
        }}
        .card:hover .card-icon {{
            background: var(--accent-1);
            color: #fff;
            transform: scale(1.1);
        }}

        .card h2 {{
            font-size: 28px; font-weight: 800; margin-bottom: 12px;
        }}
        .card p {{
            font-size: 16px; color: var(--text-secondary); line-height: 1.6;
            margin-bottom: 30px; flex-grow: 1;
        }}

        .card-link {{
            display: flex; align-items: center; gap: 8px;
            font-weight: 800; color: var(--accent-1);
            text-transform: uppercase; letter-spacing: 1px; font-size: 14px;
        }}
        .card-link span {{ transition: transform 0.3s; }}
        .card:hover .card-link span {{ transform: translateX(8px); }}

        footer {{
            margin-top: auto;
            padding: 60px 24px;
            background: #0f172a;
            color: #fff;
        }}
        .footer-inner {{
            max-width: 1200px; margin: 0 auto;
            display: flex; justify-content: space-between; align-items: center;
            flex-wrap: wrap; gap: 40px;
        }}
        .contact-info h3 {{ font-size: 18px; font-weight: 800; margin-bottom: 4px; }}
        .contact-info p {{ font-size: 14px; opacity: 0.7; }}

        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 40px; }}
            .cards-container {{ grid-template-columns: 1fr; }}
            .footer-inner {{ flex-direction: column; text-align: center; }}
        }}
    </style>
</head>
<body>
    <div class="bg-decor"></div>
    
    <header>
        <div class="logo">
            {logo_html}
        </div>
        <div style="font-size: 13px; font-weight: 600; opacity: 0.6;">HERRAMIENTAS PROFESIONALES</div>
    </header>

    <main>
        <section class="hero">
            <h1>Expertos en Impresión <span>Digital de Gran Formato</span></h1>
            <p>Accede a nuestras herramientas exclusivas para profesionales y optimiza tu producción hoy mismo.</p>
        </section>

        <section class="cards-container">
            <a href="tarifa-dm.html" class="card">
                <div>
                    <div class="card-icon">💰</div>
                    <h2>Tarifa de Materiales</h2>
                    <p>Accede a nuestro catálogo completo de soportes Flexibles y Rígidos con precios siempre actualizados. Crea tu propia selección y consulta disponibilidad en segundos.</p>
                </div>
                <div class="card-link">Explorar Tarifas <span>→</span></div>
            </a>

            <a href="https://comparativa-plotters2.vercel.app" class="card">
                <div>
                    <div class="card-icon">🖨️</div>
                    <h2>Comparador de Plotters</h2>
                    <p>Análisis técnico y financiero de maquinaria. Calcula el TCO (Coste Total de Propiedad), ROI y compara tecnologías para tomar la mejor decisión de inversión.</p>
                </div>
                <div class="card-link">Comparar Equipos <span>→</span></div>
            </a>
        </section>
    </main>

    <footer>
        <div class="footer-inner">
            <div class="contact-info">
                <h3>José Miguel García</h3>
                <p>Digital Market Andalucía</p>
                <p>657 65 27 06 | josemiguel@digital-market.es</p>
            </div>
            <div style="text-align: right; opacity: 0.5; font-size: 13px;">
                © 2026 Digital Market SL.<br>Herramientas desarrolladas para el sector gráfico.
            </div>
        </div>
    </footer>
</body>
</html>'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("Updated index.html with logo-dm.png")
