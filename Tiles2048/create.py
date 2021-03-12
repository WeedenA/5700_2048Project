def _create(userParms):
    result = dict.fromkeys(['grid', 'score', 'Integrity', 'status'])
    result['grid'] = '0'
    result['score'] = 0
    result['Integrity'] = 'somehashthing'
    result['status'] = 'pass/fail' 
    return result
