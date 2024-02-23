import os
import heapq
import argparse


class Memory:
	def __init__(self):
		pass
	
	def setup(self, num_pages, page_size):
		self.num_pages = num_pages
		self.page_size = page_size
		self.data = [[None for _ in range(page_size)] for _ in range(num_pages)]
		self.heap = []

	def __getitem__(self, key):
		return self.data[key]

	def read(self, page_num, offset):
		return self.data[page_num][offset]

	def write(self, page_num, offset, value):
		self.data[page_num][offset] = value

	def clean_page(self, page_num):
		for i in range(self.page_size):
			self.data[page_num][i] = None

	def clean_cell(self, page_num, offset):
		self.data[page_num][offset] = None

	def __str__(self):
		return str(self.data)
	

class Sort:
	def __init__(self, merge_type):
		self.merge_type = merge_type
	
	@staticmethod
	def process_file(file_name):
		print(f"Processing file {file_name}")
		MEMORY[1][1] = 0  # chunks = 0
		MEMORY[1][0] = 0 # n = 0
		with open(file_name, 'r') as file:
			MEMORY[1][2] = 0  # i = 0
			while True:
				try:
					MEMORY[0][MEMORY[1][2]] = int(next(file).strip())
					MEMORY[1][0] += 1  # n += 1
					MEMORY[1][2] += 1  # i += 1
					if MEMORY[1][2] == MEMORY.page_size:
						yield MEMORY[0]
						MEMORY[1][1] += 1  # chunks += 1
						MEMORY.clean_page(0)
						MEMORY[1][2] = 0  # i = 0
				except StopIteration:
					break
			if MEMORY[1][2] > 0:
				yield MEMORY[0]
				MEMORY[1][1] += 1
				MEMORY.clean_page(0)

	@staticmethod
	def save_chunks(chunks, file_name):
		with open(file_name, 'w') as file:
			while True:
				try:
					chunk = next(chunks)
					MEMORY[1][2] = 0  # i = 0
					while MEMORY[1][2] < MEMORY.page_size:
						if chunk[MEMORY[1][2]] is None:
							break
						file.write(str(chunk[MEMORY[1][2]]) + '\n')
						MEMORY[1][2] += 1
				except StopIteration:
					break
			MEMORY.clean_cell(1, 2)  # i = None

	@staticmethod
	def read_chunks(file_name):
		with open(file_name, 'r') as file:
			while True:
				try:
					MEMORY[1][2] = 0  # i = 0
					while MEMORY[1][2] < MEMORY.page_size:
						MEMORY[0][MEMORY[1][2]] = int(next(file).strip())	# chunk.append(int(file.readline().strip()))
						MEMORY[1][2] += 1	# i += 1
						MEMORY[1][0] += 1	# n += 1
					yield MEMORY[0]
					MEMORY[1][1] += 1	# chunks += 1
					MEMORY.clean_page(0)
				except StopIteration:
					break
			if MEMORY[1][2] > 0:
				yield
				MEMORY[1][1] += 1
				MEMORY.clean_page(0)
			# MEMORY.clean_cell(1, 2) # i = None
	
	@staticmethod
	def sort_chunk():
		MEMORY[1][2] = 0
		while MEMORY[1][2] < MEMORY.page_size:
			MEMORY[1][3] = 0
			while MEMORY[1][3] < MEMORY.page_size - 1 - MEMORY[1][2]:
				if MEMORY[0][MEMORY[1][3]] > MEMORY[0][MEMORY[1][3] + 1]:
					MEMORY[0][MEMORY[1][3]], MEMORY[0][MEMORY[1][3] + 1] = MEMORY[0][MEMORY[1][3] + 1], MEMORY[0][MEMORY[1][3]]
				MEMORY[1][3] += 1
			MEMORY[1][2] += 1

		MEMORY.clean_cell(1, 2)  # i = None
		MEMORY.clean_cell(1, 3)  # j = None

	@staticmethod
	def save_chunk(file_name):
		chunk = MEMORY[0]
		with open(file_name, 'w') as file:
			MEMORY[1][2] = 0  # i = 0
			while MEMORY[1][2] < MEMORY.page_size:
				if chunk[MEMORY[1][2]] is None:
					break
				file.write(str(chunk[MEMORY[1][2]]) + '\n')
				MEMORY[1][2] += 1
		MEMORY.clean_cell(1, 2)

	def sort_chunks(self):
		MEMORY[1][-1] = self.read_chunks('temp/processed_data.txt')
		MEMORY[1][4] = 0  # k = 1
		MEMORY[1][1] = 0  # chunks = 0
		MEMORY[1][0] = 0  # n = 0
		while True:
			try:
				next(MEMORY[1][-1])
				self.sort_chunk()
				self.save_chunk(f'temp/sorted_chunk_{MEMORY[1][4]}.txt')
				MEMORY[1][4] += 1
			except StopIteration:
				MEMORY.clean_cell(1, 2)
				MEMORY.clean_cell(1, 4)  # k = None
				break

	@staticmethod
	def read_files():
		MEMORY[1][2] = 0  # i = 0
		MEMORY[1][3] = 0  # j = 0
		while MEMORY[1][2] < MEMORY[1][1]:  # while i < n_files
			MEMORY[0][MEMORY[1][3]] = open(f'temp/sorted_chunk_{MEMORY[1][2]}.txt', 'r')
			MEMORY[1][2] += 1
			MEMORY[1][3] += 1
			if MEMORY[1][3] == MEMORY.page_size:
				yield
				MEMORY[1][3] = 0
				MEMORY.clean_page(0)
		yield
		MEMORY.clean_page(0)
		MEMORY.clean_cell(1, 2)  # i = None
		MEMORY.clean_cell(1, 3)  # j = None

	@staticmethod
	def merge_some_files(merged_file_name):
		MEMORY[1][4] = 0  # k = 0
		MEMORY[1][-1] = 0  # Accumulator
		MEMORY.heap = []
		while MEMORY[1][4] < MEMORY[1][3]:  # while k < MEMORY_SIZE
			MEMORY[1][-1] = int(next(MEMORY[0][MEMORY[1][4]]).strip())
			heapq.heappush(MEMORY.heap, (MEMORY[1][-1], MEMORY[1][4]))
			MEMORY[1][4] += 1
		with open(merged_file_name, 'w') as merged_file:
			while MEMORY.heap:
				MEMORY[1][-1], MEMORY[1][4] = heapq.heappop(MEMORY.heap)
				merged_file.write(str(MEMORY[1][-1]) + '\n')
				MEMORY[1][-1] = next(MEMORY[0][MEMORY[1][4]], None)
				if MEMORY[1][-1] is not None:
					MEMORY[1][-1] = int(MEMORY[1][-1].strip())
					heapq.heappush(MEMORY.heap, (MEMORY[1][-1], MEMORY[1][4]))

	def merge_all_files(self, file_name):
		while MEMORY[1][1] > 1:
			MEMORY[1][-2] = 0  # i = group count = 0
			MEMORY[1][-3] = self.read_files()  # generator for each file
			while True:
				try:
					next(MEMORY[1][-3])
					self.merge_some_files('temp/merged.txt')
					os.rename('temp/merged.txt', f'temp/sorted_chunk_{MEMORY[1][-2]}.txt')
					MEMORY[1][-2] += 1
				except StopIteration:
					break
			MEMORY[1][1] = MEMORY[1][-2]

		os.rename('temp/sorted_chunk_0.txt', file_name)
		os.system("rm -rf temp")
		MEMORY.clean_page(1)

	def sort_file(self, input_file, output_file):
		# If the temp directory does not exist, create it
		if not os.path.exists('temp'):
			os.makedirs('temp')
		print("Processing file")
		chunks = self.process_file(input_file)
		print("Saving chunks")
		self.save_chunks(chunks, 'temp/processed_data.txt')
		print("Sorting chunks")
		self.sort_chunks()
		print("Merging chunks")
		self.merge_all_files(output_file)
		print("File sorted and saved")


MEMORY = Memory()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--input-file", help="File to sort", required=True)
	parser.add_argument("--memory-size", type=int, help="Memory size", required=True)
	parser.add_argument("--output-file", type=str, help="Output file name", required=True)
	args = parser.parse_args()
	MEMORY.setup(2, args.memory_size)
	sorting = Sort('bubble')
	sorting.sort_file(args.input_file, args.output_file)


if __name__ == "__main__":
	main()

