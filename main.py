from data_loader.mpra_data_loader import MPRADataLoader as DataLoader
from models.conv_model import ConvModel as Model
from trainers.trainer import Trainer as Trainer
from utils.dirs import create_dirs
from utils.fetch_args import fetch_args

def main():
    # capture the config path from the run arguments
    # then process the json configuration file
    config = fetch_args()

    # create the experiments dirs
    create_dirs([config.tensorboard_log_dir, config.checkpoint_dir])

    print('Create the data generator.')
    train_data_loader = DataLoader(config, 'train')
    valid_data_loader = DataLoader(config, 'valid')

    print('Create the model.')
    model = Model(config)

    print('Create the trainer')
    trainer = Trainer(model.model, train_data_loader, valid_data_loader, config)

    print('Start training the model.')
    trainer.train()


if __name__ == '__main__':
    main()