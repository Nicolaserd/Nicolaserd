<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documento HTML con JavaScript</title>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        let textoEscrito = document.getElementById("textoDescriptivo");
        let texto = "Nicolas Inchaustegui Gonzalez";
        let indice = 0;
      
        function agregarLetra() {
          textoEscrito.textContent += texto.charAt(indice);
          indice++;
          if (indice < texto.length) {
            setTimeout(agregarLetra, 100); // Intervalo entre letras (en milisegundos)
          }
        }
      
        agregarLetra(); // Iniciar la animación de escritura
      });
    </script>
</head>

<h1 align="center" id="textoDescriptivo" >Hello, I'm Nicolas.</h1>



## Introduction


Hey everyone! As a programmer, being adaptable and self-managing is crucial to me. I tackle every challenge with energy and determination, seeing them as opportunities to innovate and grow. My ability to adjust to changes and stay focused allows me to build solid, user-friendly solutions, driving technological advancement forward.

## I’m currently working on 
-  I’m currently working on an application to connect companies with coworkings (backend)

## Recent projects.
- Registration for Jcofaith: <a href="https://clases-front-jcofaith.vercel.app/" target="_blank">https://clases-front-jcofaith.vercel.app/ </a>
- An app for an e-commerce platform backend. <a>https://github.com/Nicolaserd/EcommerceNicolas.git </a>
- I made a full-stack application for managing appointments. <a> https://github.com/Nicolaserd/Gestionturnos.git </a>

## Pending projects
- An application for sending WhatsApp messages and integrating an AI chatbot.

## Contact me

<a href="https://www.linkedin.com/in/nicolas-inchaustegui-gonzalez-b25246205/" target="_blank">
<img src="https://cdn-icons-png.flaticon.com/128/3536/3536505.png" style="height: 20px;"/>
</a>






<!--
**Nicolaserd/Nicolaserd** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
