from src.matrix import principal_component_analysis as PCA
from src.image import read_image, show_images, resize_image, to_gray, to_pb
from src.imports import logger, np

IMAGE_PATH = "data/raw/museu.jpg"

def demonstrate_color_and_resizing(original_image: np.ndarray):
    """Demonstra conversões de cor e redimensionamento da imagem."""
    logger.info("Demonstrando conversões de cor...")
    colored_imgs = [original_image, to_gray(original_image), to_pb(original_image)]
    show_images(colored_imgs, titles=["Original", "Escala de Cinza", "Preto e Branco"])

    logger.info("Demonstrando redimensionamento da imagem...")
    resized_imgs = [
        original_image,
        resize_image(original_image, (100, 100)),
        resize_image(original_image, (50, 50)),
    ]
    show_images(resized_imgs, titles=["Original", "100x100", "50x50"])


def demonstrate_pca_compression(original_image: np.ndarray):
    """Demonstra a compressão de imagem usando PCA."""
    logger.info("Demonstrando PCA para compressão de imagem...")

    gray_image = to_gray(original_image)

    max_components = min(gray_image.shape)
    
    components_to_test = [c for c in [100, 50, 20] if c < max_components]
    
    if not components_to_test:
        logger.warning(f"A imagem é muito pequena ({gray_image.shape}) para os componentes de PCA selecionados. Pulando a demonstração de PCA.")
        return

    pca_reconstructions = [PCA(gray_image, n) for n in components_to_test]

    images_to_show = [gray_image] + pca_reconstructions
    titles = ["Original em Escala de Cinza"] + [f"PCA com {n} componentes" for n in components_to_test]

    show_images(images_to_show, titles=titles)

def main():
    """Função principal para executar as demonstrações de processamento de imagem."""
    original_image = read_image(IMAGE_PATH)
    
    demonstrate_color_and_resizing(original_image)
    demonstrate_pca_compression(original_image)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error(f"Ocorreu um erro inesperado: {e}", exc_info=True)