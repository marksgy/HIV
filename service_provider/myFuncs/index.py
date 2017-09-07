
def welcomePage(request):
    name=request.session.get('name', 'anybody')
    myDict={"name":name}
    return myDict

