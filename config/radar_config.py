# ==============================================================================
# config/radar_config.py
# ==============================================================================
from dataclasses import dataclass

@dataclass
class RadarConfig:
    """Configuración centralizada del sistema FMCW"""
    # Parámetros del radar
    Fs: float = 20000           # Hz - Frecuencia de muestreo
    N: int = 128                # Número de muestras por rampa
    B: float = 200e6            # Hz - Ancho de banda
    c: float = 3e8              # m/s - Velocidad de la luz
    fc: float = 24e9            # Hz - Frecuencia central de la antena
    
    # Puertos seriales
    port_I: str = "COM3"
    port_Q: str = "COM5"
    baudrate: int = 115200
    timeout: float = 2.0
    
    # Parámetros de procesamiento
    N_SAMPLES: int = 200
    velocity_threshold: float = 0.01  # m/s para detectar movimiento
    samples_per_ramp = 128 # Muestras a tomar para el procesamiento en cada rampa
    
    # Tamaños de colas
    queue_size: int = 5
    
    # Calculados
    @property
    def T(self) -> float:
        """Duración del chirp"""
        return (1 / self.Fs) * self.N
    
    @property
    def K(self) -> float:
        """Tasa de cambio de frecuencia"""
        return self.B / self.T















