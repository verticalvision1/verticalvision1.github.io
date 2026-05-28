with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

print("```
```text?code_stdout&code_event_index=2
```html
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vertical Vision | Vertikální video marketing pro firmy</title>
    <style>
        :root {
            --primary: #8a3ffc;
            --primary-gradient: linear-gradient(135deg, #a259ff 0%, #00c6ff 100%);
            --bg-dark: #0b0c10;
            --bg-card: #1f2833;
            --text-light: #f5f6fa;
            --text-muted: #c5a880;
            --accent: #00c6ff;
            --text-gray: #a0a5b5;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            scroll-behavior: smooth;
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-light);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Header & Navigation */
        header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: rgba(11, 12, 16, 0.95);
            backdrop-filter: blur(10px);
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo-box {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--text-light);
        }

        .logo-img {
            height: 45px;
            width: 45px;
            object-fit: contain;
            border-radius: 8px;
        }

        .logo-text {
            font-size: 1.4rem;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        nav ul {
            display: flex;
            list-style: none;
            gap: 30px;
        }

        nav a {
            color: var(--text-gray);
            text-decoration: none;
            font-size: 1rem;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        nav a:hover, nav a.active {
            color: var(--text-light);
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 120px 20px 8px 20px;
            position: relative;
            background: radial-gradient(circle at 50% 30%, rgba(138, 63, 252, 0.15) 0%, rgba(11, 12, 16, 0) 70%);
        }

        .hero-content {
            max-width: 850px;
            z-index: 2;
        }

        .hero h1 {
            font-size: 3.5rem;
            font-weight: 900;
            line-height: 1.2;
            margin-bottom: 25px;
            letter-spacing: -1px;
        }

        .hero h1 span {
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            font-size: 1.25rem;
            color: var(--text-gray);
            margin-bottom: 40px;
            max-width: 650px;
            margin-left: auto;
            margin-right: auto;
        }

        .cta-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
        }

        .btn {
            display: inline-block;
            padding: 14px 30px;
            border-radius: 30px;
            font-size: 1rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .btn-primary {
            background: var(--primary-gradient);
            color: #fff;
            box-shadow: 0 4px 15px rgba(138, 63, 252, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(138, 63, 252, 0.6);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.05);
            color: var(--text-light);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        /* Sections General */
        section {
            padding: 100px 20px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-header {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-header h2 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 15px;
        }

        .section-header h2 span {
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .section-header p {
            color: var(--text-gray);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
        }

        /* About Us Section */
        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
        }

        .about-text h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: var(--text-light);
        }

        .about-text p {
            color: var(--text-gray);
            margin-bottom: 20px;
            font-size: 1.05rem;
        }

        .about-features {
            list-style: none;
        }

        .about-features li {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 15px;
            color: var(--text-light);
            font-weight: 500;
        }

        .about-features li::before {
            content: "✓";
            color: #00c6ff;
            font-weight: bold;
            font-size: 1.2rem;
        }

        .about-visual {
            background: linear-gradient(135deg, rgba(162, 89, 255, 0.1) 0%, rgba(0, 198, 255, 0.1) 100%);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            position: relative;
        }

        .about-visual img {
            max-width: 180px;
            filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5));
            animation: float 4s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        /* Services Grid */
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }

        .service-card {
            background: var(--bg-card);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 40px 30px;
            border-radius: 16px;
            transition: all 0.3s ease;
        }

        .service-card:hover {
            transform: translateY(-5px);
            border-color: #00c6ff;
            box-shadow: 0 10px 30px rgba(0, 198, 255, 0.1);
        }

        .service-icon {
            font-size: 2.5rem;
            margin-bottom: 20px;
            display: inline-block;
        }

        .service-card h3 {
            font-size: 1.4rem;
            margin-bottom: 15px;
        }

        .service-card p {
            color: var(--text-gray);
            font-size: 0.95rem;
        }

        /* Cooperation Steps (Jak probíhá spolupráce) */
        .steps-container {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }

        .step {
            display: flex;
            gap: 30px;
            margin-bottom: 40px;
            position: relative;
        }

        .step-number {
            background: var(--primary-gradient);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 1.2rem;
            flex-shrink: 0;
            box-shadow: 0 4px 10px rgba(138, 63, 252, 0.3);
        }

        .step-content {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 25px;
            border-radius: 12px;
            width: 100%;
        }

        .step-content h3 {
            font-size: 1.25rem;
            margin-bottom: 10px;
            color: #fff;
        }

        .step-content p {
            color: var(--text-gray);
            font-size: 0.95rem;
        }

        /* Contact Section */
        .contact-grid {
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 50px;
        }

        .contact-info {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .contact-info h3 {
            font-size: 1.8rem;
            margin-bottom: 20px;
        }

        .contact-info p {
            color: var(--text-gray);
            margin-bottom: 30px;
        }

        .info-item {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 20px;
        }

        .info-icon {
            background: rgba(0, 198, 255, 0.1);
            color: var(--accent);
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
        }

        .info-text h4 {
            font-size: 0.9rem;
            color: var(--text-gray);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .info-text p {
            margin-bottom: 0;
            color: #fff;
            font-weight: 500;
        }

        .contact-form {
            background: var(--bg-card);
            padding: 40px;
            border-radius: 16px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-size: 0.9rem;
            color: var(--text-gray);
        }

        .form-group input, .form-group textarea {
            width: 100%;
            padding: 12px 16px;
            background: rgba(0,0,0,0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px;
            color: #fff;
            font-size: 1rem;
            transition: all 0.3s ease;
        }

        .form-group input:focus, .form-group textarea:focus {
            outline: none;
            border-color: var(--accent);
            box-shadow: 0 0 10px rgba(0, 198, 255, 0.2);
        }

        /* Footer */
        footer {
            background: #060709;
            padding: 40px 20px;
            text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            color: var(--text-gray);
            font-size: 0.9rem;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav ul {
                display: none; /* simple hidden for mobile, can be enhanced */
            }
            
            .hero h1 {
                font-size: 2.4rem;
            }
            
            .about-grid, .contact-grid {
                grid-template-columns: 1fr;
            }
            
            .cta-buttons {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <a href="#" class="logo-box">
                <img src="data:image/jpeg;base64,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...
```html\n" + html_content + "\n```")