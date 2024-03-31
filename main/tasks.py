from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Movie


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    mvznmbr = Movie.objects.filter(status__in  = ['coming-up', 'starting', 'running']).values('id')
    for m in mvznmbr:
        old_rank = Movie.objects.filter(id=m['id']).values('ranking')[0]['ranking']
        Movie.objects.filter(id=m['id']).update(ranking = int(old_rank+10))
    logger.info(mvznmbr)#"Movies, from creation (status='coming_up') to launch (status='running') have been ranked by 10 more.")