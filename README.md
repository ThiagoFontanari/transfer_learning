# BASIC DEFINITIONS OF TRANSFER LEARNING | DEFINIÇÕES BÁSICAS DE TRANFER LEARNING

	According to the official Keras website (https://keras.io/), the Transfer Learning technique consists of taking advantage of the learning of a certain model (or feature extraction) about a given problem and applying it to a new, similar problem, where there is not a dataset with enough volume to carry out a complete training. The workflow for applying the transfer learning method generally follows these steps:

		1 - Instantiate a base model and load pre-trained weights into it;
		2 - Freeze all layers in the base model by setting base_model.trainable = False;
		3 - Create a new model on top of the output of one (or several) layers from the base model;
		4 - Train your new model on your new dataset;

	In this example, the ResNet50 network was used as a base and the training weights of this network were downloaded from the IMAGENET database. The proposal is to verify how the network behaves when it is trained for use in the identification of skin lesions and to verify if it is monkeypox or not. The model was fed from a database downloaded from Kaggle (https://www.kaggle.com/datasets/nafin59/monkeypox-skin-lesion-dataset). The ResNet50 network used has a total of 23587712 total parameters, of which 23534592 are trainable. For this example, an accuracy of 0.9863 was achieved.

_______________________________________________________________________________________________________________


	De acordo com o site oficial do Keras (https://keras.io/), a técnica de Transfer Learning consiste em aproveitar o aprendizado de um determinado modelo (ou extração de features) sobre um dado problema e aplicá-lo em um novo problema semelhante, onde não se dispõe de um dataset com volume suficiente para realização de um treinamento completo. O fluxo de trabalho para a aplicação do método de transfer learning segue, de maneira geral, os seguintes passos:

		1 - Instanciar um modelo base e carregar os pesos do treinamento realizado;
		2 - "Congelar" as camadas do modelo base, "modelo_base.trainable=False";
		3 - Criar um novo modelo sobre a camada de saída do modelo de base;
		4 - Treinar o novo modelo com o novo dataset;


	Neste exemplo, foi utilizada como base a rede ResNet50 e foram baixados os pesos de treinamento desta rede com a base de dados IMAGENET. A proposta é verificar como se comporta a rede ao ser treinada para utilização na identificação de lesões de pele e verificar se trata-se de varíola dos macacos ou não. O modelo foi alimentado com uma base de dados baixada do Kaggle (https://www.kaggle.com/datasets/nafin59/monkeypox-skin-lesion-dataset). A rede ResNet50 utilizada possui um total de 23587712 parâmetros totais, sendo que 23534592 são treináveis. Para este exemplo, foi atingida uma acurácia de 0.9863.

