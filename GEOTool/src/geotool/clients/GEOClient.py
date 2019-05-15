from abc import ABC
from geotool.constants.Constants import *
import time
import requests
import threading
import sys


class GEOClient(ABC):
	__running = True

	def __init__(self, url, service, request, version, format, coord, size, block_size=1, offset=(0, 0)):
		self.url = url
		self.service = service
		self.request = request
		self.version = version
		self.format = format
		self.params = "?"
		self.coord = coord
		self.size = size
		self.block_size = block_size
		self.offset = offset

	def generate_params(self):
		self.add_param("SERVICE", self.service)
		self.add_param("REQUEST", self.request)
		self.add_param("VERSION", self.version)
		self.add_param("FORMAT", self.format)
		self.add_param("BBOX", self.generate_bbox())

	def generate_bbox(self):
		x = self.coord[X] + (self.offset[0]*self.block_size)
		y = self.coord[Y] + (self.offset[1]*self.block_size)
		x2 = x + self.block_size * self.size[HEIGHT]
		y2 = y + self.block_size * self.size[WIDTH]

		return "{},{},{},{}".format(x, y, x2, y2)

	@staticmethod
	def progress_bar_worker():
		while GEOClient.__running:
			print(".", end="")
			sys.stdout.flush()
			time.sleep(0.1)

	@staticmethod
	def start_progress_bar():
		GEOClient.__running = True
		t = threading.Thread(target=GEOClient.progress_bar_worker)
		t.start()

	@staticmethod
	def stop_progress_bar():
		GEOClient.__running = False

	def send_request(self):
		self.generate_params()

		print("Request to: " + str(self.url) + str(self.params))
		print("Downloading", end="")
		sys.stdout.flush()
		GEOClient.start_progress_bar()
		data = requests.get(self.url + self.params)
		GEOClient.stop_progress_bar()
		print("Download completed!")
		sys.stdout.flush()

		return data

	def add_param(self, key, value):
		self.params = self.params + "&" + str(key) + "=" + str(value)
