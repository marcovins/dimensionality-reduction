from .imports import np, logger
from .image import read_image, save_image, to_pb

def matrix_multiply(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
    """
    Multiplica duas matrizes usando NumPy.
    
    Args:
        matrix_a (np.ndarray): Primeira matriz.
        matrix_b (np.ndarray): Segunda matriz.
        
    Returns:
        np.ndarray: Resultado da multiplicação das matrizes.
    """
    try:
        logger.debug("Multiplicando matrizes")
        resultado = np.dot(matrix_a, matrix_b)
        logger.info("Multiplicação de matrizes concluída com sucesso")
        return resultado
    
    except ValueError as e:
        raise ValueError(f"Erro na multiplicação de matrizes: {e}")
    
def transpose_matrix(matrix: np.ndarray) -> np.ndarray:
    """
    Transpõe uma matriz usando NumPy.
    
    Args:
        matrix (np.ndarray): Matriz a ser transposta.
        
    Returns:
        np.ndarray: Matriz transposta.
    """
    try:
        if matrix.ndim != 2:
            raise ValueError("O array de imagem deve ser bidimensional (preto e branco).")
        logger.debug("Transpondo matriz")
        transposta = np.transpose(matrix)
        logger.info("Transposição de matriz concluída com sucesso")
        return transposta
    except Exception as e:
        raise ValueError(f"Erro ao transpor a matriz: {e}")

def covariance_matrix(X_centered: np.ndarray, n_amostras: int) -> np.ndarray:
    """
    Calcula a matriz de covariância de uma matriz centralizada.
    
    Args:
        X_centered (np.ndarray): Matriz de entrada já centralizada (amostras x variáveis).
        n_amostras (int): Número de amostras.
        
    Returns:
        np.ndarray: Matriz de covariância.
    """
    try:
        logger.debug("Calculando matriz de covariância")

        cov_matrix = (X_centered.T @ X_centered) / (n_amostras - 1)

        logger.info("Matriz de covariância calculada com sucesso")
        return cov_matrix
    
    except Exception as e:
        raise ValueError(f"Erro ao calcular a matriz de covariância: {e}")
    
def principal_component_analysis(X: np.ndarray, n_components: int) -> np.ndarray:
    """
    Realiza Análise de Componentes Principais (PCA) em uma matriz.
    
    Args:
        X (np.ndarray): Matriz de entrada (amostras x variáveis).
        n_components (int): Número de componentes principais a serem retornados.
        
    Returns:
        np.ndarray: Matriz transformada com os componentes principais.
    """
    try:
        if n_components > min(X.shape):
            raise ValueError(f"n_components ({n_components}) não pode ser maior que min(n_amostras, n_features) = {min(X.shape)}")
        
        logger.debug("Iniciando PCA")

        # Centralizar os dados por coluna
        media = np.mean(X, axis=0)
        X_centered = X - media

        # Matriz de covariância: (X^T X) / (n - 1)
        n_amostras = X.shape[0]
        
        # Calcular a matriz de covariância
        cov_matrix = covariance_matrix(X_centered, n_amostras)
        
        # Obter os autovalores e autovetores
        eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
        
        # Ordenar os autovalores e autovetores
        sorted_indices = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[sorted_indices]
        eigenvectors = eigenvectors[:, sorted_indices]
        
        # Selecionar os primeiros n componentes
        principal_components = eigenvectors[:, :n_components]
        
        # Transformar os dados
        X_transformed = X_centered @ principal_components
        logger.info("PCA concluído com sucesso")
        return X_transformed
    except Exception as e:
        raise ValueError(f"Erro ao realizar PCA: {e}")

if __name__ == "__main__":
    array_test = np.array([[1, 2], [3, 4]])
    print("Matriz original:")
    print(array_test)
    pca_test = principal_component_analysis(array_test, 2)
    print("Matriz de PCA:")
    print(pca_test)