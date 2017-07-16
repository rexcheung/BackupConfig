BACKUP_DIR = 'file'

HOME = '/home/zxbin'


class file_path():
	directry = ''
	file_name = ''

	def __init__(self, directory, file_name) -> None:
		super().__init__()
		self.directry = directory
		self.file_name = file_name


file_list = [
	file_path(HOME, '.ideavimrc'),
	file_path(HOME, '.vimrc')
]
