_base_ = 'cascade_rcnn_swin_small_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco.py'

# SPECIFY THE NUMBER OF CLASSES OF CUSTOM DATASET
model = dict(
    roi_head=dict(
        bbox_head=[
            dict(
                type='Shared2FCBBoxHead',
                num_classes=),
            dict(
                type='Shared2FCBBoxHead',
                num_classes=),
            dict(
                type='Shared2FCBBoxHead',
                num_classes=)]))


dataset_type = 'COCODataset'

# SPECIFY THE CLASS NAMES
classes = ('class name 1',
    'class name 2',...)

data = dict(
    train=dict(
        img_prefix='Swin-Transformer-Object-Detection/configs/PROJECT_NAME/train/',
        classes=classes,
        ann_file='Swin-Transformer-Object-Detection/configs/PROJECT_NAME/train/TRAIN_FILE.json'),
    val=dict(
        img_prefix='Swin-Transformer-Object-Detection/configs/PROJECT_NAME/test/',
        classes=classes,
        ann_file='Swin-Transformer-Object-Detection/configs/PROJECT_NAME/test/TEST_FILE.json'),
    test=dict(
        img_prefix='Swin-Transformer-Object-Detection/configs/PROJECT_NAME/test/',
        classes=classes,
        ann_file='Swin-Transformer-Object-Detection/configs/PROJECT_NAME/test/TEST_FILE.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/cascade_mask_rcnn_swin_small_patch4_window7.pth'

