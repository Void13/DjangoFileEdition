from FileEditor.forms import EditorForm
from django.http import *
from django.template import Template, context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import os

def FileEditor(request):
	form = None;
	requestedFlName = '';
	sPrevFolderName = '';
	fullFolderName = '';
	folder_list = [];
	file_list = [];
	
	if request.GET:
		if request.GET.get("fl", None):
			requestedFlName = request.GET["fl"];
			
		if request.GET.get("prev_folder", None):
			sPrevFolderName = request.GET["prev_folder"];
	
	fullFolderName = settings.STARTFOLDER + sPrevFolderName + requestedFlName;
	
	print "\n";
	print "Full folder name: %s" % fullFolderName;
	print "Requested folder: %s" % requestedFlName;
	print "Previous folder: %s" % sPrevFolderName;
	print "\n";
	
	if os.path.isdir(fullFolderName):
		dfList = [os.path.join(fullFolderName, f_or_d) for f_or_d in os.listdir(fullFolderName)]
		for file_or_dir in dfList:
			if os.path.isdir(file_or_dir):
				folder_list.append(file_or_dir.split('\\')[-1]);
			if os.path.isfile(file_or_dir):
				file_list.append(file_or_dir.split('\\')[-1]);
			
		return render_to_response(
				"FileEditing.html", 
			{
				'title': requestedFlName,
				'prev_folder': sPrevFolderName, 
				'folder_list': folder_list, 
				'file_list': file_list 
			},
			context_instance=RequestContext(request));
	else:
		response = HttpResponse(open(fullFolderName, "rb"), mimetype='application/force-download');
		#response['Content-Disposition'] = 'attachment';
		response['Content-Disposition'] = 'attachment; filename=%s' % requestedFlName;
		return response;