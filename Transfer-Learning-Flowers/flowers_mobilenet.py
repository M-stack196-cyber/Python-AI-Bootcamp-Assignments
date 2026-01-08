# Transfer Learning Project: Flower Species Classification
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Load pre-trained MobileNetV2
base_model = MobileNetV2(weights='imagenet', 
                         include_top=False, 
                         input_shape=(224,224,3))
base_model.trainable = False  # Freeze base layers

# Add custom layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
output = Dense(5, activation='softmax')(x)  # 5 flower classes

# Create final model
model = Model(inputs=base_model.input, outputs=output)

# Compile Model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Model Summary
model.summary()

print("Transfer Learning Model with MobileNetV2 created successfully!")