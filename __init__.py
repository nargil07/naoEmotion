# Standard scientific Python imports
from naoqi import ALProxy
#
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 50630)
tts.say("Allo le monde ! ", "French")
#
#
# import httplib, urllib, base64
# headers = {
#     # Request headers
#     'Content-Type': 'application/octet-stream',
#     'Ocp-Apim-Subscription-Key': '281f633d67934f50ae690175f0b271a9',
# }
#
# params = urllib.urlencode({
# })
#
# try:
#     conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/emotion/v1.0/recognize?%s" % params, open('test/test.jpg', 'rb').read(), headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print(" {0}".format(e))


#recognizer = cv2.createLBPHFaceRecognizer()
#
# event_png_pair = []
# i = 0
# size = 512, 512
# files = glob.glob('picture/*.*')
# array_image = np
# i = 0
# data = []
# classes = []
# for file in glob.glob('picture/colere/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     data.append(in_data.flatten())
#     classes.append("colere")
#
# for file in glob.glob('picture/doute/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     data.append(in_data.flatten())
#     classes.append("doute")
#
# for file in glob.glob('picture/triste/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     data.append(in_data.flatten())
#     classes.append("triste")
#
# for file in glob.glob('picture/souriant/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     data.append(in_data.flatten())
#     classes.append("souriant")
#
# for file in glob.glob('picture/rire/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     data.append(in_data.flatten())
#     classes.append("rire")
#
# for file in glob.glob('picture/blase/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     data.append(in_data.flatten())
#     classes.append("blase")

#
# classifier = svm.SVC(gamma=0.001)
# classifier.fit(data, classes)
#
# tests = []
# for file in glob.glob('test/*.*'):
#     edges = Image.open(file)
#     in_data = np.asarray(edges, dtype=np.uint8)
#     tests.append(in_data.flatten())
#
# predicted = classifier.predict(tests)
# print classes
# print predicted



# # The digits dataset
# digits = datasets.load_digits()
#
# # The data that we are interested in is made of 8x8 images of digits, let's
# # have a look at the first 4 images, stored in the `images` attribute of the
# # dataset.  If we were working from image files, we could load them using
# # matplotlib.pyplot.imread.  Note that each image must have the same size. For these
# # images, we know which digit they represent: it is given in the 'target' of
# # the dataset.
# images_and_labels = list(zip(digits.images, digits.target))
# for index, (image, label) in enumerate(images_and_labels[:4]):
#     plt.subplot(2, 4, index + 1)
#     plt.axis('off')
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.title('Training: %i' % label)
#
# # To apply a classifier on this data, we need to flatten the image, to
# # turn the data in a (samples, feature) matrix:
# n_samples = len(digits.images)
# data = digits.images.reshape((n_samples, -1))
#
# # Create a classifier: a support vector classifier
# classifier = svm.SVC(gamma=0.001)
#
# # We learn the digits on the first half of the digits
# classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])
#
# # Now predict the value of the digit on the second half:
# expected = digits.target[n_samples / 2:]
# predicted = classifier.predict(data[n_samples / 2:])
#
# print("Classification report for classifier %s:\n%s\n"
#       % (classifier, metrics.classification_report(expected, predicted)))
# print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
#
# images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
# for index, (image, prediction) in enumerate(images_and_predictions[:4]):
#     plt.subplot(2, 4, index + 5)
#     plt.axis('off')
#     plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
#     plt.title('Prediction: %i' % prediction)
#
# plt.show()
