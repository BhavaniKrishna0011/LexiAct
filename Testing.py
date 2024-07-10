# import tensorflow as tf
# import time
# import numpy as np

# # Check TensorFlow version
# print(f"TensorFlow Version: {tf.__version__}")

# # Create a simple dataset
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# x_train, x_test = x_train / 255.0, x_test / 255.0

# # Reshape and normalize the data
# x_train = x_train.reshape(-1, 28, 28, 1).astype('float32')
# x_test = x_test.reshape(-1, 28, 28, 1).astype('float32')

# # Define a simple CNN model
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
#     tf.keras.layers.MaxPooling2D((2, 2)),
#     tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
#     tf.keras.layers.MaxPooling2D((2, 2)),
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(10, activation='softmax')
# ])

# # Compile the model
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# # Measure the time taken to train the model
# start_time = time.time()

# # Train the model
# model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=1)

# # Measure the time taken
# end_time = time.time()
# elapsed_time = end_time - start_time

# # Evaluate the model
# test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

# # Print the results
# print(f"Training Time: {elapsed_time:.2f} seconds")
# print(f"Test Accuracy: {test_acc:.4f}")

# # Print if using GPU or CPU
# if tf.test.is_gpu_available():
#     print("Using GPU for computation")
# else:
#     print("Using CPU for computation")

import tensorflow as tf

print(f"TensorFlow Version: {tf.__version__}")
