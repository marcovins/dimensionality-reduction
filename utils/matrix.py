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

def covariance_matrix(X: np.ndarray) -> np.ndarray:
    """
    Calcula a matriz de covariância de uma matriz usando NumPy.
    
    Args:
        X (np.ndarray): Matriz de entrada (amostras x variáveis).
        
    Returns:
        np.ndarray: Matriz de covariância.
    """
    try:
        logger.debug("Calculando matriz de covariância")
        
        if X.ndim != 2:
            raise ValueError("A matriz de entrada deve ser bidimensional (2D)")
        
        # Centralizar os dados por coluna
        media = np.mean(X, axis=0)
        X_centered = X - media

        # Matriz de covariância: (X^T X) / (n - 1)
        n_amostras = X.shape[0]
        cov_matrix = (X_centered.T @ X_centered) / (n_amostras - 1)

        logger.info("Matriz de covariância calculada com sucesso")
        return cov_matrix
    
    except Exception as e:
        raise ValueError(f"Erro ao calcular a matriz de covariância: {e}")
    

if __name__ == "__main__":
    array_test = np.random.randn(4,4)
    print("Matriz original:")
    print(array_test)
    cov_test = covariance_matrix(array_test)
    print("Matriz de covariância:")
    print(cov_test)