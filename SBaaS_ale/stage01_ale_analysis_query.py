#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_ale_analysis_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_ale_analysis_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_ale_analysis':data_stage01_ale_analysis
                        };
        self.set_supportedTables(tables_supported);
    # query data from data_stage01_ale_analysis
    def get_analysis_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_ale_analysis).filter(
                    data_stage01_ale_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_ale_analysis.used_.is_(True)).all();
            analysis_id_O = []
            experiment_id_O = []
            ale_id_O = []
            analysis_type_O = []
            analysis_O = {};
            if data: 
                for d in data:
                    analysis_id_O.append(d.analysis_id);
                    experiment_id_O.append(d.experiment_id);
                    ale_id_O.append(d.ale_id);
                    analysis_type_O.append(d.analysis_type);
                analysis_id_O = list(set(analysis_id_O))
                experiment_id_O = list(set(experiment_id_O))
                lineage_name_O = list(set(lineage_name_O))
                ale_id_O = list(set(ale_id_O))
                analysis_type_O = list(set(analysis_type_O))
                analysis_O={
                        'analysis_id':analysis_id_O,
                        'experiment_id':experiment_id_O,
                        'ale_id':ale_id_O,
                        'analysis_type':analysis_type_O};
                
            return analysis_O;
        except SQLAlchemyError as e:
            print(e);
    def get_experimentIDAndALEID_analysisID_dataStage01ResequencingAnalysis(self,analysis_id_I):
        '''Query rows that are used from the analysis'''
        try:
            data = self.session.query(data_stage01_ale_analysis.experiment_id,
                    data_stage01_ale_analysis.ale_id).filter(
                    data_stage01_ale_analysis.analysis_id.like(analysis_id_I),
                    data_stage01_ale_analysis.used_.is_(True)).group_by(
                    data_stage01_ale_analysis.experiment_id,
                    data_stage01_ale_analysis.ale_id).order_by(
                    data_stage01_ale_analysis.experiment_id.asc(),
                    data_stage01_ale_analysis.ale_id.asc()).all();
            experiment_id_O = []
            ale_id_O = []
            if data: 
                for d in data:
                    experiment_id_O.append(d.experiment_id);
                    ale_id_O.append(d.ale_id);                
            return  experiment_id_O,ale_id_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01AleAnalysis(self, data_I):
        '''add rows of data_stage01_ale_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_ale_analysis(d
                        #d['analysis_id'],
                        #d['experiment_id'],
                        #d['ale_id'],
                        #d['analysis_type'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def update_dataStage01AleAnalysis(self,data_I):
        '''update rows of data_stage01_ale_analysis'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_ale_analysis).filter(
                            data_stage01_ale_analysis.id == d['id']).update(
                            {'analysis_id':d['analysis_id'],
                            'experiment_id':d['experiment_id'],
                            'ale_id':d['ale_id'],
                            'analysis_type':d['analysis_type'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def reset_dataStage01_ale_analysis(self,analysis_id_I=None):
        try:
            if analysis_id_I:
                reset = self.session.query(data_stage01_ale_analysis).filter(data_stage01_ale_analysis.analysis_id.like(analysis_id_I)).delete(synchronize_session=False);
            else:
                reset = self.session.query(data_stage01_ale_analysis).delete(synchronize_session=False);
            self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def drop_dataStage01_ale_analysis(self):
        try:
            data_stage01_ale_analysis.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_ale_analysis(self):
        try:
            data_stage01_ale_analysis.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);