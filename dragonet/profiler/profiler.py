
from processor import textProcessor as tp
import xml.etree.ElementTree as ET
import os

class Profiler:
	"""docstring for ClassName"""
	def __init__(self):
		self.data = None


	def fetch_questions(self):
		file_path = "/home/nafis/projects/JobsMarkt/hunting_gizmo/XMLs/registration"
		xml_file = os.path.join(file_path, 'registration.xml')
		tree = ET.parse(xml_file)
		root = tree.getroot()

		tags = [(child.tag,child.text) for child in root ]
		return tags
		

	def pro_labelling(self, tag_ques_pair):
		print(tag_ques_pair)
		labelled_str = tp.textProcessor().put_frequency(tag_ques_pair[1])
		print(labelled_str)
		return labelled_str




		


