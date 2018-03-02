import jenkins
import time


server = jenkins.Jenkins('http://192.168.1.200:8080', username='yixin', password='yixinkeji')
def build_jobs():
    for job in server.get_all_jobs():
        print(job['fullname'])
# server.build_job('dev_appadmin_admin')

# build_jobs()
# print(server.get_views())
# print(server.get_all_jobs())
# print(server.get_running_builds())
# a=server.get_running_builds()
# print(len(a))
# time.sleep(3)
#get run_builds jobs dic
# run_list={}
# for x in range(len(a)):
#     run_list[str(a[x]['name'])]=str(a[x]['number'])
# server.get_build_console_output('dev_appadmin_admin',95)

print(server.get_views())
# print(server.get_view_config())
# print(server.get_view_config('all'))
# print(server._get_view_jobs('all'))

# def Jviews():
#     JvNameList=[]
#     JvL=server.get_views()
#     for i in range(len(JvL)):
#         JvNameList.append(JvL[i]['name'])
#     return JvNameList
def Jviews():
    JvNameDic={}
    JvL=server.get_views()
    for i in range(len(JvL)):
        jobs=JvJobs(JvL[i]['name'])
        JvNameDic[JvL[i]['name']]=jobs
    return JvNameDic

def JvJobs(viewName):
    JobName=[]
    JJobList=server._get_view_jobs(view_name=viewName)
    for i in range(len(JJobList)):
        JobName.append(JJobList[i]['name'])
    return JobName

