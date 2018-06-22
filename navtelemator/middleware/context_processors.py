from navtelemator import services


# makes database variable available to all files
def database_processor(request):
    return {'database': services.correct_database_version()}