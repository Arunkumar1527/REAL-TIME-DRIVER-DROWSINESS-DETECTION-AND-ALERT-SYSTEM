import argparse
import dlib

print("[INFO] evaluating shape predictor...")
error = dlib.test_shape_predictor(r"C:\Users\A...K\Desktop\My python\labels_ibug_300W_test",r"C:\Users\A...K\Desktop\My python\eye_predictor.dat")
print("[INFO] error: {}".format(error))