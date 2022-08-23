from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
import keras
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.optimizers import Adam

# Loading train, validation and tests datasets
# Carregando os datasets para treinamento, validação e testes
train_ds = keras.utils.image_dataset_from_directory(
    directory='dataset/train_ds/',
    labels='inferred',
    label_mode='categorical',
	batch_size=32,
    image_size=(224,224))
validation_ds = keras.utils.image_dataset_from_directory(
    directory='dataset/validation_ds/',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(224, 224))

# Instantiating a ResNet50 network model as base. Here the weights of the training performed with the imagenet
# base are downloaded through the weights parameter. Also, the top layer is removed by giving the
# include_top=False parameter

# Instanciando um modelo da rede ResNet50 como base. Aqui são baixados os pesos do treinamento com a base imagenet
# através do parâmetro weights. Também é removida a camada top do modelo através do parâmetro
# include_top=False
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3), classes=2)
base_model.summary()

# Freezing the base model layers
# Congelando as camadas do modelo de base
base_model.trainable = False
base_model.summary()

# Building the new model, adding the trained layers from the base model
# Construindo o novo modelo e adicionando as camadas já treinadas do modelo base
new_model = keras.Sequential()
new_model.add(base_model)
new_model.add(Flatten())
new_model.add(Dense(512, activation='relu'))
new_model.add(Dense(2, activation='softmax'))
new_model.summary()

# Compiling the new model from the base model and the layers implemented after transfer learning
# Compilando o novo modelo a partir do modelo base e das camadas implementadas após o transfer learning
new_model.compile(optimizer=Adam(lr=0.001),loss='categorical_crossentropy',metrics=['accuracy'])

# Training the new model
# Treinando o modelo novo
new_model.fit(train_ds, epochs=10, validation_data=validation_ds)
