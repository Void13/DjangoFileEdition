from FileEditor.forms import EditorForm
from django.http import *
from django.template import Template, context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
import os

ModifiedSTARTFOLDER = settings.STARTFOLDER;

def FileEditor(request):
	form = None;
	requestedFolderName = '';
	sPrevFolderName = '';
	folder_list = [];
	file_list = [];
	global ModifiedSTARTFOLDER;
	
	if request.GET and request.GET["folder"]:
		requestedFolderName = request.GET["folder"];
	
	fullFolderName = settings.STARTFOLDER + requestedFolderName;
	
	if request.GET and request.GET["back"] and request.GET["back"] == 'true':
		ModifiedSTARTFOLDER = ModifiedSTARTFOLDER + requestedFolderName;
	else:
		ModifiedSTARTFOLDER = ModifiedSTARTFOLDER.;
		
	if requestedFolderName != '':
		sPrevFolderName = requestedFolderName[:-1 - len(requestedFolderName.rsplit('\\')[-1])];
	
	# если юзер идёт вперёд, то надо прибавить к текущему модифиеду новую папку
	# если юзер идёт назад, то надо отнять у текущего модифиеда одну папку
	
	dfList = [os.path.join(fullFolderName, f_or_d) for f_or_d in os.listdir(fullFolderName)]
	for file_or_dir in dfList:
		if os.path.isdir(file_or_dir):
			folder_list.append(file_or_dir.split('\\')[-1]);
		if os.path.isfile(file_or_dir):
			file_list.append(file_or_dir.split('\\')[-1]);

	if os.path.isdir(fullFolderName):
		return render_to_response(
				"FileEditing.html", 
			{
				'title': requestedFolderName,
				'prev_folder': sPrevFolderName, 
				'folder_list': folder_list, 
				'file_list': file_list 
			},
			context_instance=RequestContext(request));
	else:
		return HttpResponse(open(fullFolderName), content_type='application/text');