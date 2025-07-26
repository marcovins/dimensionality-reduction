from .imports import Image, np, logger, plt

def read_image(image_path:str) -> np.ndarray:
    """
    Lê uma imagem do caminho especificado e a converte em um array NumPy.
    
    Args:
        image_path (str): Caminho para a imagem a ser lida.
        
    Returns:
        np.ndarray: Array NumPy representando a imagem.
    """
    try:
        logger.debug(f"Lendo a imagem do caminho: {image_path}")
        imagem = Image.open(image_path)
        logger.info(f"Imagem lida com sucesso: {image_path}")
        return np.array(imagem)
    
    except Exception as e:
            raise ValueError(f"Erro ao ler a imagem: {e}")
    
def save_image(image_array: np.ndarray, image_name:str) -> None:
    """
    Salva um array NumPy como uma imagem no diretório padrão.
    
    Args:
        image_array (np.ndarray): Array NumPy representando a imagem a ser salva.
        image_name (str): Nome da imagem a ser salva.
    Returns:
        None
    """
    try:
        save_path = f"data/processed/{image_name}"
        logger.debug(f"Salvando a imagem no caminho: {save_path}")
        imagem = Image.fromarray(image_array)
        imagem.save(save_path)
        logger.info(f"Imagem salva com sucesso: {save_path}")
    
    except Exception as e:
        raise ValueError(f"Erro ao salvar a imagem: {e}")
    
def resize_image(image_array: np.ndarray, size: tuple) -> np.ndarray:
    """
    Redimensiona um array NumPy representando uma imagem para o tamanho especificado.
    
    Args:
        image_array (np.ndarray): Array NumPy representando a imagem a ser redimensionada.
        size (tuple): Tupla contendo as novas dimensões (largura, altura).
        
    Returns:
        np.ndarray: Array NumPy representando a imagem redimensionada.
    """
    try:
        logger.debug(f"Redimensionando a imagem para o tamanho: {size}")
        imagem = Image.fromarray(image_array)
        imagem_redimensionada = imagem.resize(size)
        logger.info("Imagem redimensionada com sucesso")
        return np.array(imagem_redimensionada)
    
    except Exception as e:
        raise ValueError(f"Erro ao redimensionar a imagem: {e}")
    
def to_gray(image_array: np.ndarray) -> np.ndarray:
    """
    Converte um array NumPy representando uma imagem para escala de cinza.
    
    Args:
        image_array (np.ndarray): Array NumPy representando a imagem a ser convertida.
        
    Returns:
        np.ndarray: Array NumPy representando a imagem em escala de cinza.
    """
    try:
        logger.debug("Convertendo a imagem para escala de cinza")
        if image_array.ndim != 3 or image_array.shape[2] != 3:
            raise ValueError("O array de imagem deve ter três canais (RGB).")
        imagem_gray = (0.299 * image_array[:, :, 0] + 0.587 * image_array[:, :, 1] + 0.114 * image_array[:, :, 2]).astype(np.uint8)
        logger.info("Imagem convertida para escala de cinza com sucesso")
        return np.array(imagem_gray)
    
    except Exception as e:
        raise ValueError(f"Erro ao converter a imagem para escala de cinza: {e}")
    
def to_pb(image_array: np.ndarray, threshold:int = 128) -> np.ndarray:
    """
    Converte um array NumPy representando uma imagem para o formato de bytes (protobuf).
    
    Args:
        image_array (np.ndarray): Array NumPy representando a imagem a ser convertida.
        
    Returns:
        np.ndarray: Array NumPy representando a imagem em formato de bytes.
    """
    try:
        threshold = threshold if 0 < threshold < 255 else 128
        logger.debug("Convertendo a imagem para formato de bytes")
        image_gray = to_gray(image_array)
        image_pb = np.where(image_gray >= threshold, 255, 0).astype(np.uint8)
        logger.info("Imagem convertida para formato de bytes com sucesso")
        return image_pb
    
    except Exception as e:
        raise ValueError(f"Erro ao converter a imagem para formato de bytes: {e}")
    
def to_rgb(image_array: np.ndarray, with_color:bool = False) -> np.ndarray:
    """
    Converte um array NumPy representando uma imagem em preto e branco para RGB.
    
    Args:
        image_array (np.ndarray): Array NumPy representando a imagem em preto e branco.
        with_color (bool): Se True, a imagem recebera cores aleatórias.
    Returns:
        np.ndarray: Array NumPy representando a imagem convertida para RGB.
    """
    try:
        if with_color:
            logger.debug("Convertendo a imagem de bytes para RGB com cores aleatórias")
            if image_array.ndim != 2:
                image_array = to_gray(image_array)
            # Cria uma imagem RGB com cores aleatórias
            random_colors = np.random.randint(0, 256, size=(image_array.shape[0], image_array.shape[1], 3), dtype=np.uint8)
            rgb_image = np.where(image_array[:, :, None] > 0, random_colors, 0)
            logger.info("Imagem convertida para RGB com cores aleatórias")
            return rgb_image
        logger.debug("Convertendo a imagem de bytes para RGB")
        if image_array.ndim != 2:
            image_array = to_gray(image_array)
        rgb_image = np.stack((image_array,) * 3, axis=-1)
        logger.info("Imagem convertida para RGB com sucesso")
        return rgb_image
    
    except Exception as e:
        raise ValueError(f"Erro ao converter a imagem para RGB: {e}")
    
def show_image(image_array: np.ndarray, title: str = None) -> None:
    """
    Exibe um array NumPy representando uma imagem.
    
    Args:
        image_array (np.ndarray): Array NumPy representando a imagem a ser exibida.
        title (str, opcional): Título a ser exibido acima da imagem.
    """
    try:
        if not isinstance(image_array, np.ndarray):
            raise TypeError("A entrada deve ser um array NumPy.")

        logger.debug("Exibindo a imagem")
        plt.figure(figsize=(6, 6))
        cmap = 'gray' if image_array.ndim == 2 else None
        plt.imshow(image_array, cmap=cmap)
        plt.axis('off')
        if title:
            plt.title(title)
        plt.show()
        logger.info("Imagem exibida com sucesso")
    
    except Exception as e:
        raise ValueError(f"Erro ao exibir a imagem: {e}")
    
def show_images(images: list, titles: list = None) -> None:
    """
    Exibe uma lista de arrays NumPy representando imagens.
    
    Args:
        images (list): Lista de arrays NumPy representando as imagens a serem exibidas.
        titles (list, opcional): Lista de títulos a serem exibidos acima das imagens.
    """
    try:
        if not isinstance(images, list) or not all(isinstance(img, np.ndarray) for img in images):
            raise TypeError("A entrada deve ser uma lista de arrays NumPy.")
        
        logger.debug("Exibindo múltiplas imagens")
        n = len(images)
        plt.figure(figsize=(15, 5))
        
        for i, img in enumerate(images):
            plt.subplot(1, n, i + 1)
            cmap = 'gray' if img.ndim == 2 else None
            plt.imshow(img, cmap=cmap)
            plt.axis('off')
            if titles and i < len(titles):
                plt.title(titles[i])
        
        plt.tight_layout()
        plt.show()
        logger.info("Imagens exibidas com sucesso")
    
    except Exception as e:
        raise ValueError(f"Erro ao exibir as imagens: {e}")
    
if __name__ == "__main__":
    # Exemplo de uso
    try:
        img_array = read_image("data/raw/museu.jpg")
        
        gray_array = to_gray(img_array)
        save_image(gray_array, "imagem_gray.jpg")

        pb_array = to_pb(img_array)
        save_image(pb_array, "imagem_pb.jpg")
        
        rgb_array = to_rgb(img_array, True)
        save_image(rgb_array, "imagem_rgb.jpg")
        show_images([img_array, gray_array, pb_array, rgb_array],
            titles=["Original", "Gray", "PB", "RGB com cores aleatórias"])
        
    except ValueError as e:
        logger.error(e)