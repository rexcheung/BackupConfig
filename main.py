import os
import Constant
from shutil import copyfile


def check_backup(file_name):
	file = Constant.BACKUP_DIR + '/' + file_name
	# print(os.path.exists(file))
	return os.path.exists(file)


def is_replace():
	text = input('目标备份文件已经存在，是否覆盖(yes)? :')
	if text == 'yes':
		return True
	else:
		return False


def main():
	for i in range(0, len(Constant.file_list)):
		file = Constant.file_list[i]
		# print(file.directry+"/"+file.file_name)
		full_path = file.directry + '/' + file.file_name
		# print(os.path.exists(full_path))
		if check_backup(file.file_name):
			print(file.file_name)
			if is_replace():
				copyfile(full_path, Constant.BACKUP_DIR + '/' + file.file_name)
		else:
			copyfile(full_path, Constant.BACKUP_DIR + '/' + file.file_name)


main()
