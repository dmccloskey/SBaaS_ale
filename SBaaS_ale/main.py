import sys
sys.path.append('C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base')
from SBaaS_base.postgresql_settings import postgresql_settings
from SBaaS_base.postgresql_orm import postgresql_orm

# read in the settings file
filename = 'C:/Users/dmccloskey-sbrg/Google Drive/SBaaS_base/settings_metabolomics.ini';
pg_settings = postgresql_settings(filename);

# connect to the database from the settings file
pg_orm = postgresql_orm();
pg_orm.set_sessionFromSettings(pg_settings.database_settings);
session = pg_orm.get_session();
engine = pg_orm.get_engine();

# your app...
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_LIMS')
sys.path.append(pg_settings.datadir_settings['drive']+'/SBaaS_ale')
sys.path.append(pg_settings.datadir_settings['github']+'/io_utilities')
sys.path.append(pg_settings.datadir_settings['github']+'/calculate_utilities')

#make the analysis table
from SBaaS_ale.stage01_ale_analysis_execute import stage01_ale_analysis_execute
analysis01 = stage01_ale_analysis_execute(session,engine,pg_settings.datadir_settings);
#analysis01.drop_dataStage01_ale_analysis();
#analysis01.initialize_dataStage01_ale_analysis();
#analysis01.reset_dataStage01_ale_analysis('ALEsKOs01_OxicEvo04tpiA');
#analysis01.import_dataStage01AleAnalysis_add('data/tests/analysis_ale/140823_ALE_ALEsKOs01_dataStage01_ale_analysis.csv');

#make the ale trajectories methods tables
from SBaaS_ale.stage01_ale_trajectories_execute import stage01_ale_trajectories_execute
trajectories01 = stage01_ale_trajectories_execute(session,engine,pg_settings.datadir_settings);
#trajectories01.drop_dataStage01_ale_trajectories();
#trajectories01.initialize_dataStage01_ale_trajectories();
#trajectories01.reset_dataStage01_ale_trajectories('ALEsKOs01');
#trajectories01.import_dataStage01AleTrajectories_matlab('ALEsKOs01',
#          'data/tests/analysis_ale/ALEsKOs_trajectories.mat');
trajectories01.export_dataStage01AleTrajectories_js('ALEsKOs01_OxicEvo04tpiA');