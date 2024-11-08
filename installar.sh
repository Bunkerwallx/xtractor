#!/bin/bash

# Inicializa colores para mensajes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Función para mostrar mensajes de error
error_exit() {
    echo -e "${RED}[ERROR]${NC} $1"
    exit 1
}

# Detecta el sistema operativo y configura el gestor de paquetes
echo -e "${GREEN}Detectando el sistema operativo...${NC}"
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
else
    error_exit "Sistema operativo no soportado"
fi

# Instalar dependencias según el sistema operativo
install_dependencies() {
    case $OS in
        ubuntu|debian)
            echo -e "${GREEN}Usando apt para instalar dependencias...${NC}"
            sudo apt update && sudo apt install -y python3 python3-pip || error_exit "Fallo al instalar dependencias en Debian/Ubuntu"
            ;;
        fedora)
            echo -e "${GREEN}Usando dnf para instalar dependencias...${NC}"
            sudo dnf install -y python3 python3-pip || error_exit "Fallo al instalar dependencias en Fedora"
            ;;
        arch)
            echo -e "${GREEN}Usando pacman para instalar dependencias...${NC}"
            sudo pacman -Sy --noconfirm python python-pip || error_exit "Fallo al instalar dependencias en Arch"
            ;;
        gentoo)
            echo -e "${GREEN}Usando emerge para instalar dependencias...${NC}"
            sudo emerge --update --newuse python || error_exit "Fallo al instalar dependencias en Gentoo"
            ;;
        macos)
            echo -e "${GREEN}Usando brew para instalar dependencias...${NC}"
            if ! command -v brew &> /dev/null; then
                error_exit "Homebrew no está instalado. Por favor, instálalo primero desde https://brew.sh"
            fi
            brew install python || error_exit "Fallo al instalar dependencias en macOS"
            ;;
        *)
            error_exit "Sistema operativo no soportado"
            ;;
    esac
}

# Instala Python y pip si no están disponibles
install_dependencies

# Instalar dependencias desde requirements.txt
echo -e "${GREEN}Instalando dependencias de requirements.txt...${NC}"
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt || error_exit "Fallo al instalar las dependencias"
else
    error_exit "Archivo requirements.txt no encontrado"
fi

# Crear directorios necesarios
echo -e "${GREEN}Creando directorios de resultados...${NC}"
mkdir -p ~/resultados || error_exit "Fallo al crear directorio ~/resultados"

# Mensaje final de éxito
echo -e "${GREEN}Instalación completada exitosamente.${NC}"

