
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import _init_paths

import os

os.environ['CUDA_DEVICE_ORDER'] = "PCI_BUS_ID"
# print("Choose GPU")
# print(type(opt.gpus_str))
# print(opt.gpus_str)
os.environ['CUDA_VISIBLE_DEVICES'] = "0"

import sys
import cv2
import json, time
import copy
import numpy as np
from opts import opts
from detector import Detector


image_ext = ['jpg', 'jpeg', 'png', 'webp']
video_ext = ['mp4', 'mov', 'avi', 'mkv']
time_stats = ['tot', 'load', 'pre', 'net', 'dec', 'post', 'merge', 'display']
class_name = ['pedestrian','car','van','truck','bus']
obj_category = ['1', '4','5','6', '9']
class_colors = [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 0, 0)]

def demo(opt):
	lsdir = sorted(os.listdir(opt.demo))[0:1]
	opt.debug = max(opt.debug, 1)
	detector = Detector(opt)
	num_imgs = 0
	start = time.time()
	for kk, dirr in enumerate(lsdir):
		folder = os.path.join(opt.demo, dirr)
		print(folder)
		is_video = False
		# print("Demo on images sequences")
		if os.path.isdir(folder):
			image_names = []
			ls = os.listdir(folder)
			for file_name in sorted(ls):
				ext = file_name[file_name.rfind('.') + 1:].lower()
				if ext in image_ext:
					image_names.append(os.path.join(folder, file_name))
		else:
			image_names = [folder]
	  
		if opt.debug < 5:
			detector.pause = False
		cnt = 0
		results = {}
		# f = open('../visdrone_detections/5/80_epochs/'+str(dirr)+'.txt', 'w')
		while True:
			# print("Frame No: "+str(cnt))
			if is_video:
				_, img = cam.read()
				if img is None:
					save_and_exit(opt, out, results, out_name)
			else:
				if cnt < len(image_names):
					img = cv2.imread(image_names[cnt])
					seq_num = str(int(image_names[cnt].split('/')[-1].split('.')[0]))

				else:
					break
			cnt += 1
			# resize the original video for saving video results
			if opt.resize_video:
				img = cv2.resize(img, (opt.video_w, opt.video_h))

				# skip the first X frames of the video
			if cnt < opt.skip_first:
				continue

			# track or detect the image.
			if cnt == 1:
				print(img.shape)

			ret = detector.run(img)
			num_imgs = num_imgs+1

			# # log run time
			# time_str = 'frame {} |'.format(cnt)
			# results[cnt] = ret['results']
			# for j, ll in enumerate(ret['results']):
			# 	# print(ll)
			# 	score = ll['score']
			# 	trd = ll['tracking_id']
			# 	# print(type(score))
			# 	bb = ll['bbox']
			# 	label = obj_category[int(ll['class'])-1]
			# 	p = (int(bb[0]), int(bb[1]))

				# f.write(seq_num+','+str(trd)+','+str(int(bb[0]))+','+str(int(bb[1]))+','+str(int(bb[2]-bb[0]))+','+str(int(bb[3]-bb[1]))+','+str(score)+','+str(label)+',-1,-1\n')
				# cv2.putText(img, label, p, cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 255), 3, cv2.LINE_AA)
				# cv2.rectangle(img, (bb[0], bb[1]), (bb[2], bb[3]), class_colors[ll['class']-1], 2)
				# img2 = img
				# img2 = cv2.resize(img2, None, fx=0.75, fy=0.75, interpolation=cv2.INTER_CUBIC)
				# cv2.imshow("Image", img2)
				# cv2.waitKey(0)
	      
	# esc to quit and finish saving video
			if cv2.waitKey(1) == 27:
				save_and_exit(opt, out, results, out_name)
				return
		# f.close()
	end = time.time()
	fps = int(num_imgs/(end-start))
	print("FPS: "+str(fps))

def save_and_exit(opt, out=None, results=None, out_name=''):
	if opt.save_results and (results is not None):
		save_dir =  '../results/{}_results.json'.format(opt.exp_id + '_' + out_name)
		print('saving results to', save_dir)
		json.dump(_to_list(copy.deepcopy(results)), open(save_dir, 'w'))
	if opt.save_video and out is not None:
		out.release()
		sys.exit(0)

def _to_list(results):
	for img_id in results:
		for t in range(len(results[img_id])):
			for k in results[img_id][t]:
				if isinstance(results[img_id][t][k], (np.ndarray, np.float32)):
					results[img_id][t][k] = results[img_id][t][k].tolist()
	return results

if __name__ == '__main__':
	opt = opts().init()
	demo(opt)


