/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      './app/templates/**/*.html',
      './app/static/src/**/*.css',
      './app/routes/**/*.py'
    ],
    theme: {
      extend: {
        colors: {
          dark: {
            100: '#1a1a1a',
            200: '#333333',
            300: '#4d4d4d',
            400: '#666666',
            500: '#808080',
            600: '#999999',
            700: '#b3b3b3',
            800: '#cccccc',
            900: '#e6e6e6'
          },
          primary: {
            DEFAULT: '#0d6efd', // Color azul oscuro para elementos principales
          },
          secondary: {
            DEFAULT: '#6c757d', // Color gris oscuro para elementos secundarios
          },
          accent: {
            DEFAULT: '#dc3545', // Color rojo para acentos o botones de acción
          }
        },
      },
    },
    plugins: [],
  }
  