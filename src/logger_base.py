import logging as log

log.basicConfig(
    level=log.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%H:%H:%S',
    handlers=[
        log.FileHandler('data_layer.log'),
        log.StreamHandler()
    ]
)

if __name__ == "__main__":
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critico')