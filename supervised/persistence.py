base_path = '/content/drive/MyDrive/TFGNatalia/DAVIS-2017-detectron-masks'
experiment_type = 'maskrcnn_vf'


paths = {
    'rl': {
        'models.select': base_path + '',
        'models.assign': base_path + '',
        'masks': base_path + '',
        'rewards': base_path + ''
    },
    'supervised': {
        'models.select': base_path + '',
        'models.assign': base_path + '',
        'masks': base_path + ''
    },
    'oracle': {
        'masks': base_path + '/oracle/masks/'
    }
}