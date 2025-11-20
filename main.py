

# ==============================================================================
# main.py
# ==============================================================================
import queue
from config.radar_config import RadarConfig
from hardware.serial_reader import SerialChannelReader
from processing.radar_processor import RadarProcessor
from visualization.plotter import RadarPlotter

def main():
    print("="*70)
    print("           SISTEMA FMCW RADAR I/Q ")
    print("="*70)
    
    # Configuración
    config = RadarConfig()
    
    # Colas de comunicación
    queue_I = queue.Queue(maxsize=config.queue_size)
    queue_Q = queue.Queue(maxsize=config.queue_size)
    queue_results = queue.Queue(maxsize=config.queue_size)
    
    # Crear componentes
    reader_I = SerialChannelReader(
        config.port_I, "I", config.baudrate, 
        config.timeout, config.N_SAMPLES, queue_I,
        config.samples_per_ramp
    )
    reader_Q = SerialChannelReader(
        config.port_Q, "Q", config.baudrate, 
        config.timeout, config.N_SAMPLES, queue_Q,
        config.samples_per_ramp
    )
    processor = RadarProcessor(config, queue_I, queue_Q, queue_results)
    plotter = RadarPlotter(config, queue_results)
    
    # Iniciar sistema
    reader_I.start()
    reader_Q.start()
    processor.start()
    
    print("[MAIN] Sistema iniciado")
    
    # Visualización (blocking)
    try:
        plotter.start()
    except KeyboardInterrupt:
        print("\n[MAIN] Deteniendo sistema...")
        reader_I.stop()
        reader_Q.stop()
        processor.stop()
        print("[MAIN] Sistema detenido")

if __name__ == "__main__":
    main()