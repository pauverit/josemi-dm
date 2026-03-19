import json
import base64
import os

def generate():
    # Load the extracted data
    if not os.path.exists('product_data_v6.json'):
        print("Error: product_data_v6.json not found.")
        return
        
    with open('product_data_v6.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Encode logo as base64 if it exists
    logo_html = '<div class="logo-text" style="color:var(--accent-1); font-weight:800; font-size:24px;">DIGITAL MARKET</div>'
    logo_path = 'logo-dm.png'
    if os.path.exists(logo_path):
        with open(logo_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            logo_html = f'<img src="data:image/png;base64,{encoded_string}" alt="Digital Market Logo" style="height: 60px; width: auto;">'

    # Prepare data as JS
    data_js = json.dumps(data, ensure_ascii=False)

    html_template = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Market — Tarifa de Productos</title>
    <meta name="description" content="Catálogo de precios de materiales para impresión digital. Selección y consulta de presupuestos.">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f8fafc;
            --bg-card: #ffffff;
            --bg-card-hover: #f1f5f9;
            --accent-1: #0088cc;
            --accent-2: #006699;
            --accent-3: #e0f2fe;
            --text-primary: #0f172a;
            --text-secondary: #334155;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --success: #22c55e;
            --whatsapp: #25D366;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Outfit', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            padding-bottom: 100px;
        }

        header {
            position: sticky; top: 0; z-index: 100;
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(10px);
            border-bottom: 3px solid var(--accent-1);
            padding: 0 24px;
        }
        .header-inner {
            max-width: 1400px; margin: 0 auto;
            display: flex; align-items: center; justify-content: space-between;
            height: 100px;
        }
        .logo { display: flex; align-items: center; gap: 15px; }

        .contact-top {
            display: flex; flex-direction: column; align-items: flex-end; gap: 2px;
            font-size: 13px; color: var(--text-secondary);
        }
        .contact-top b { color: var(--accent-1); font-size: 15px; }

        .search-container {
            position: relative; flex: 1; margin: 0 40px;
        }
        #searchInput {
            width: 100%; padding: 12px 18px 12px 45px;
            background: #f1f5f9; border: 2px solid transparent;
            border-radius: 12px; color: var(--text-primary);
            transition: all 0.2s; font-family: inherit;
        }
        #searchInput:focus { outline: none; border-color: var(--accent-1); background: #fff; }
        .search-icon {
            position: absolute; left: 15px; top: 50%; transform: translateY(-50%);
            color: var(--accent-1);
        }

        .tabs-container { max-width: 1400px; margin: 0 auto; padding: 32px 24px 0; }
        .main-tabs { display: flex; gap: 8px; }
        .main-tab {
            padding: 16px 36px; background: #f1f5f9; border: none;
            border-radius: 12px 12px 0 0; color: var(--text-secondary);
            font-weight: 700; cursor: pointer; transition: all 0.2s;
            font-family: inherit; text-transform: uppercase; letter-spacing: 0.5px;
        }
        .main-tab.active { background: var(--accent-1); color: #fff; }

        .content { max-width: 1400px; margin: 0 auto; padding: 0 24px 60px; }
        .panel-layout { display: grid; grid-template-columns: 310px 1fr; gap: 40px; }
        .tab-panel {
            display: none; background: #fff; border: 2px solid var(--accent-1);
            border-radius: 0 20px 20px 20px; padding: 35px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        }
        .tab-panel.active { display: block; }

        .category-nav { position: sticky; top: 130px; max-height: calc(100vh - 200px); overflow-y: auto; padding-right: 15px; }
        .cat-btn {
            width: 100%; padding: 14px; text-align: left;
            background: transparent; border: none; border-radius: 10px;
            color: var(--text-secondary); font-weight: 600; cursor: pointer;
            margin-bottom: 8px; transition: all 0.2s; font-family: inherit;
        }
        .cat-btn:hover { background: #f1f5f9; }
        .cat-btn.active { background: var(--accent-3); color: var(--accent-1); font-weight: 800; }

        .group-header { margin-bottom: 40px; padding-bottom: 12px; border-bottom: 4px solid var(--accent-1); }
        .group-title { color: var(--accent-1); font-size: 32px; font-weight: 900; }
        
        .subcat-section { margin-bottom: 45px; }
        .subcat-title { font-size: 20px; color: var(--text-primary); margin-bottom: 18px; font-weight: 800; border-left: 5px solid var(--accent-1); padding-left: 15px; }
        
        .product-table { width: 100%; border-collapse: collapse; margin-bottom: 25px; }
        .product-table th { text-align: left; padding: 14px; font-size: 11px; color: var(--text-muted); text-transform: uppercase; border-bottom: 2px solid #f1f5f9; letter-spacing: 1px; }
        .product-table td { padding: 16px 14px; border-bottom: 1px solid #f1f5f9; font-size: 15px; }
        .product-table tr:hover td { background: #f8fafc; }
        
        .price-tag {
            background: var(--accent-1); color: #fff; padding: 6px 14px;
            border-radius: 8px; font-weight: 800; min-width: 90px; display: inline-block; text-align: center;
        }
        .price-half { color: var(--text-muted); font-size: 11px; display: block; margin-top: 4px; font-weight: 500; }

        .add-btn {
            width: 32px; height: 32px; border-radius: 50%; border: 2px solid var(--accent-1);
            background: transparent; color: var(--accent-1); font-weight: 800; cursor: pointer;
            display: flex; align-items: center; justify-content: center; transition: all 0.2s;
        }
        .add-btn:hover { background: var(--accent-1); color: #fff; transform: scale(1.1); }
        .add-btn.added { background: var(--success); border-color: var(--success); color: #fff; }

        .request-box {
            position: fixed; bottom: 30px; right: 30px; width: 350px;
            background: #fff; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.15);
            z-index: 1000; overflow: hidden; display: none; border: 2px solid var(--accent-1);
        }
        .request-header { background: var(--accent-1); color: #fff; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }
        .request-body { padding: 20px; max-height: 400px; overflow-y: auto; }
        .request-item { display: flex; justify-content: space-between; font-size: 14px; margin-bottom: 10px; padding-bottom: 10px; border-bottom: 1px solid #eee; }
        .request-footer { padding: 20px; background: #f8fafc; display: flex; gap: 10px; flex-direction: column; }
        
        .btn { padding: 12px; border-radius: 10px; border: none; font-weight: 700; cursor: pointer; color: #fff; text-align: center; text-decoration: none; font-family: inherit; }
        .btn-wa { background: var(--whatsapp); }
        .btn-mail { background: var(--accent-1); }

        mark { background: #bfdbfe; color: #1e3a8a; }
        
        @media (max-width: 1000px) {
            .panel-layout { grid-template-columns: 1fr; }
            .category-nav { display: none; }
            .header-inner { height: auto; padding: 15px 0; flex-direction: column; gap: 15px; }
            .search-container { margin: 0; width: 100%; }
        }
    </style>
</head>
<body>
    <header>
        <div class="header-inner">
            <div class="logo">
                <a href="index.html" style="text-decoration: none; color: inherit; display: flex; align-items: center; gap: 15px;">
                    {{LOGO_HTML}}
                </a>
            </div>
            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" placeholder="Buscar materiales o marcas...">
            </div>
            <div style="display: flex; align-items: center; gap: 20px;">
                <a href="index.html" style="text-decoration: none; font-weight: 700; color: var(--accent-1); font-size: 14px; padding: 8px 16px; background: var(--accent-3); border-radius: 8px; transition: all 0.2s;">
                    🏠 Inicio
                </a>
                <div class="contact-top">
                    <span>Comercial: <b>José Miguel García</b></span>
                    <span>📞 657 65 27 06 | ✉️ josemiguel@digital-market.es</span>
                </div>
            </div>
        </div>
    </header>

    <div class="tabs-container">
        <div class="main-tabs">
            <button class="main-tab active" data-tab="flexibles">FLEXIBLES</button>
            <button class="main-tab" data-tab="rigidos">RÍGIDOS</button>
            <button class="main-tab" data-tab="tintas">TINTAS</button>
        </div>
    </div>

    <div class="content">
        <div class="tab-panel active" id="panel-flexibles">
            <div class="panel-layout">
                <div class="category-nav" id="nav-flexibles"></div>
                <div class="products-area" id="products-flexibles"></div>
            </div>
        </div>
        <div class="tab-panel" id="panel-rigidos">
            <div class="panel-layout">
                <div class="category-nav" id="nav-rigidos"></div>
                <div class="products-area" id="products-rigidos"></div>
            </div>
        </div>
        <div class="tab-panel" id="panel-tintas">
            <div class="panel-layout">
                <div class="category-nav" id="nav-tintas"></div>
                <div class="products-area" id="products-tintas"></div>
            </div>
        </div>
    </div>

    <div class="request-box" id="requestBox">
        <div class="request-header">
            <span style="font-weight: 800;">TU CONSULTA</span>
            <span style="cursor: pointer;" onclick="toggleRequest()">✕</span>
        </div>
        <div class="request-body" id="requestItems"></div>
        <div class="request-footer">
            <a href="#" class="btn btn-wa" id="waBtn" onclick="sendWhatsApp()">Confirmar por WhatsApp</a>
            <a href="#" class="btn btn-mail" id="mailBtn" onclick="sendEmail()">Confirmar por Email</a>
            <button class="btn btn-order" id="orderBtn" onclick="processOrder()" style="background: #e11d48; margin-top: 10px;">🚀 Tramitar Pedido en Portal</button>
        </div>
    </div>

    <button id="toggleBtn" onclick="toggleRequest()" style="position:fixed; bottom:30px; right:30px; background:var(--accent-1); color:#fff; width:60px; height:60px; border-radius:30px; border:none; box-shadow:0 10px 25px rgba(0,0,0,0.2); cursor:pointer; font-size:24px; z-index:999; display:none;">
        🛒 <span id="cartCount" style="position:absolute; top:-5px; right:-5px; background:red; color:#fff; font-size:12px; width:22px; height:22px; border-radius:11px; display:flex; align-items:center; justify-content:center; font-weight:800;">0</span>
    </button>

    <footer style="max-width: 1400px; margin: 40px auto; padding: 40px 24px; border-top: 1px solid var(--border); text-align: center;">
        <div style="opacity: 0.6; margin-bottom: 15px;">Digital Market Andalucía — Servicio Profesional de Impresión</div>
        <div style="font-size: 13px; color: var(--text-muted);">© 2026 Digital Market SL. Precios sujetos a cambios.</div>
    </footer>

    <script>
        const DATA = {{DATA_JS}};
        let currentCat = { flexibles: 'all', rigidos: 'all', tintas: 'all' };
        let q = '';
        let selection = [];

        function renderNav(type) {
            const nav = document.getElementById('nav-' + type);
            if (!nav) return;
            let html = `<button class="cat-btn active" onclick="setCat('${type}', 'all')">Ver todo</button>`;
            DATA[type].forEach((c, i) => {
                html += `<button class="cat-btn" onclick="setCat('${type}', ${i})">${c.name}</button>`;
            });
            nav.innerHTML = html;
        }

        window.setCat = (type, idx) => {
            currentCat[type] = idx;
            document.querySelectorAll(`#nav-${type} .cat-btn`).forEach((b, i) => {
                b.classList.toggle('active', idx === 'all' ? i === 0 : i === idx + 1);
            });
            renderProducts(type);
        };

        function renderProducts(type) {
            const area = document.getElementById('products-' + type);
            if (!area) return;
            const idx = currentCat[type];
            const cats = idx === 'all' ? DATA[type] : [DATA[type][idx]];
            
            let html = '';
            cats.forEach(c => {
                const filtered = c.subcategories.map(sc => ({
                    ...sc, products: sc.products.filter(p => match(p, sc.name, c.name))
                })).filter(sc => sc.products.length > 0);

                if (filtered.length > 0) {
                    html += `<div class="group-header"><h2 class="group-title">${hl(c.name)}</h2></div>`;
                    filtered.forEach(sc => {
                        html += `<div class="subcat-section">
                            <h3 class="subcat-title">${hl(sc.name)}</h3>
                            <table class="product-table">
                                <thead><tr>
                                    <th style="width: 50%">Producto</th>
                                    ${type === 'flexibles' || type === 'tintas' ? '<th>Detalle</th>' : ''}
                                    <th style="text-align:right">Precio</th>
                                    ${type === 'rigidos' ? '<th style="text-align:right">Detalle/Pack</th>' : ''}
                                    <th style="width: 50px"></th>
                                </tr></thead>
                                <tbody>`;
                        sc.products.forEach(p => {
                            const isAdded = selection.some(s => s.name === p.name);
                            html += `<tr>
                                <td style="font-weight: 600">${hl(p.name)}</td>
                                ${type === 'flexibles' || type === 'tintas' ? `<td>${hl(p.size || '-')}</td>` : ''}
                                <td style="text-align:right"><span class="price-tag">${fP(p.price)}€</span></td>
                                ${type === 'rigidos' ? `<td style="text-align:right">${p.price_half ? `<span class="price-half">${fP(p.price_half)}€</span>` : '-'}</td>` : ''}
                                <td><button class="add-btn ${isAdded?'added':''}" onclick="toggleItem('${p.name}', '${p.price}', '${sc.name}')">${isAdded?'✓':'+'}</button></td>
                            </tr>`;
                        });
                        html += `</tbody></table></div>`;
                    });
                }
            });
            area.innerHTML = html || '<p style="padding: 50px; text-align: center; color: #64748b">No se encontraron productos.</p>';
        }

        window.toggleItem = (name, price, cat) => {
            const idx = selection.findIndex(s => s.name === name);
            if(idx > -1) {
                selection.splice(idx, 1);
            } else {
                selection.push({name, price, cat});
            }
            updateUI();
        };

        function updateUI() {
            document.getElementById('cartCount').innerText = selection.length;
            document.getElementById('toggleBtn').style.display = selection.length > 0 ? 'block' : 'none';
            if (selection.length === 0) document.getElementById('requestBox').style.display = 'none';
            
            let html = '';
            selection.forEach((s, i) => {
                html += `<div class="request-item">
                    <div>
                        <div style="font-weight:700">${s.name}</div>
                        <div style="font-size:11px; color:#666">${s.cat}</div>
                    </div>
                    <div style="text-align:right">
                        <div style="font-weight:800">${fP(s.price)}€</div>
                        <div style="cursor:pointer; color:red; font-size:10px;" onclick="toggleItem('${s.name}')">Eliminar</div>
                    </div>
                </div>`;
            });
            document.getElementById('requestItems').innerHTML = html || 'No has seleccionado productos.';
            renderProducts('flexibles');
            renderProducts('rigidos');
            renderProducts('tintas');
        }

        window.sendWhatsApp = () => {
            let msg = "Hola José Miguel, me interesa consultar disponibilidad de estos productos:\\n\\n";
            selection.forEach(s => msg += `• ${s.name} (${fP(s.price)}€)\\n`);
            window.open(`https://wa.me/34657652706?text=${encodeURIComponent(msg)}`);
        };

        window.sendEmail = () => {
            const sub = "Consulta de Tarifa - Digital Market";
            let body = "Hola José Miguel,\\n\\nMe interesa consultar precio y disponibilidad de estos productos:\\n\\n";
            selection.forEach(s => body += `- ${s.name} (${fP(s.price)}€)\\n`);
            window.location.href = `mailto:josemiguel@digital-market.es?subject=${encodeURIComponent(sub)}&body=${encodeURIComponent(body)}`;
        };

        window.toggleRequest = () => {
            const b = document.getElementById('requestBox');
            b.style.display = b.style.display === 'block' ? 'none' : 'block';
        };

        window.processOrder = () => {
            if (selection.length === 0) return;
            const PORTAL_URL = "http://localhost:3000";
            const dataStr = JSON.stringify(selection);
            const encodedData = btoa(unescape(encodeURIComponent(dataStr)));
            window.location.href = `${PORTAL_URL}#import=${encodedData}`;
        };

        function match(p, sc, c) {
            if (!q) return true;
            return p.name.toLowerCase().includes(q) || (p.size && p.size.toLowerCase().includes(q)) || sc.toLowerCase().includes(q) || c.toLowerCase().includes(q);
        }

        function hl(t) {
            if (!q || !t) return t;
            return t.replace(new RegExp(`(${q})`, 'gi'), '<mark>$1</mark>');
        }

        function fP(p) { return parseFloat(p).toLocaleString('es-ES', { minimumFractionDigits: 2 }); }

        document.getElementById('searchInput').oninput = (e) => {
            q = e.target.value.toLowerCase().trim();
            renderProducts('flexibles');
            renderProducts('rigidos');
            renderProducts('tintas');
        };

        document.querySelectorAll('.main-tab').forEach(t => {
            t.onclick = () => {
                document.querySelectorAll('.main-tab').forEach(b => b.classList.remove('active'));
                document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
                t.classList.add('active');
                document.getElementById('panel-' + t.dataset.tab).classList.add('active');
            };
        });

        renderNav('flexibles');
        renderNav('rigidos');
        renderNav('tintas');
        renderProducts('flexibles');
        renderProducts('rigidos');
        renderProducts('tintas');
    </script>
</body>
</html>'''

    html_final = html_template.replace('{{LOGO_HTML}}', logo_html).replace('{{DATA_JS}}', data_js)

    with open('tarifa-dm.html', 'w', encoding='utf-8') as f:
        f.write(html_final)
    print("Updated web app with v6 data (3 Families).")

if __name__ == "__main__":
    generate()
