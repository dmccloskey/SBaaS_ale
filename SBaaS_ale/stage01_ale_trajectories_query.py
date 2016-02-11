#lims
from SBaaS_LIMS.lims_experiment_postgresql_models import *
from SBaaS_LIMS.lims_sample_postgresql_models import *

from .stage01_ale_trajectories_postgresql_models import *

from SBaaS_base.sbaas_base_query_update import sbaas_base_query_update
from SBaaS_base.sbaas_base_query_drop import sbaas_base_query_drop
from SBaaS_base.sbaas_base_query_initialize import sbaas_base_query_initialize
from SBaaS_base.sbaas_base_query_insert import sbaas_base_query_insert
from SBaaS_base.sbaas_base_query_select import sbaas_base_query_select
from SBaaS_base.sbaas_base_query_delete import sbaas_base_query_delete

from SBaaS_base.sbaas_template_query import sbaas_template_query

class stage01_ale_trajectories_query(sbaas_template_query):
    def initialize_supportedTables(self):
        '''Set the supported tables dict for 
        '''
        tables_supported = {'data_stage01_ale_trajectories':data_stage01_ale_trajectories,
                            'data_stage01_ale_jumps':data_stage01_ale_jumps,
                            'data_stage01_ale_stocks':data_stage01_ale_stocks
                        };
        self.set_supportedTables(tables_supported);
    # query sample name abbreviations from data_stage01_ale_trajectories
    def get_sampleNameAbbreviations_experimentID_dataStage01AleTrajectories(self,experiment_id_I):
        '''Querry sample name abbreviations that are used from the experiment'''
        try:
            sample_names = self.session.query(data_stage01_ale_trajectories.ale_id).filter(
                    data_stage01_ale_trajectories.experiment_id.like(experiment_id_I),
                    data_stage01_ale_trajectories.used_.is_(True)).group_by(
                    data_stage01_ale_trajectories.ale_id).order_by(
                    data_stage01_ale_trajectories.ale_id.asc()).all();
            sample_names_O = [];
            for sn in sample_names: sample_names_O.append(sn.ale_id);
            return sample_names_O;
        except SQLAlchemyError as e:
            print(e);
    # query rows from data_stage01_ale_rates
    def get_rows_experimentIDAndALEID_dataStage01AleTrajectories(self,experiment_id_I,ale_id_I):
        '''Querry rows for ale_ids that are used from the experiment'''
        try:
            data = self.session.query(data_stage01_ale_trajectories).filter(
                    data_stage01_ale_trajectories.experiment_id.like(experiment_id_I),
                    data_stage01_ale_trajectories.used_.is_(True),
                    data_stage01_ale_trajectories.ale_id.like(ale_id_I)).order_by(
                    data_stage01_ale_trajectories.ale_time.asc()).all();
            data_O = [];
            if data:
                for d in data:
                    data_tmp = d.__repr__dict__();
                    data_O.append(data_tmp);
            return data_O;
        except SQLAlchemyError as e:
            print(e);

    def add_dataStage01AleTrajectories(self, data_I):
        '''add rows of data_stage01_ale_trajectories'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_ale_trajectories(d
                        #d['experiment_id'],
                        #d['ale_id'],
                        #d['ale_time'],
                        #d['ale_time_units'],
                        #d['generations'],
                        #d['ccd'],
                        #d['rate'],
                        #d['rate_units'],
                        #d['used_'],
                        #d['comment_']
                                    );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01AleTrajectories(self,data_I):
        '''update rows of data_stage01_ale_trajectories'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_ale_trajectories).filter(
                            data_stage01_ale_trajectories.id == d['id']).update(
                            {
                            'experiment_id':d['experiment_id'],
                            'ale_id':d['ale_id'],
                            'ale_time':d['ale_time'],
                            'ale_time_units':d['ale_time_units'],
                            'generations':d['generations'],
                            'ccd':d['ccd'],
                            'rate':d['rate'],
                            'rate_units':d['rate_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01AleJumps(self, data_I):
        '''add rows of data_stage01_ale_jumps'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_ale_jumps(d
                        #d['experiment_id'],
                        #d['ale_id'],
                        #d['ale_time'],
                        #d['ale_time_units'],
                        #d['rate_fitted'],
                        #d['rate_fitted_units'],
                        #d['jump_region'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01AleJumps(self,data_I):
        '''update rows of data_stage01_ale_jumps'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_ale_jumps).filter(
                            data_stage01_ale_jumps.id == d['id']).update(
                            {'experiment_id':d['experiment_id'],
                            'ale_id':d['ale_id'],
                            'ale_time':d['ale_time'],
                            'ale_time_units':d['ale_time_units'],
                            'rate_fitted':d['rate_fitted'],
                            'rate_fitted_units':d['rate_fitted_units'],
                            'jump_region':d['jump_region'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def add_dataStage01AleStocks(self, data_I):
        '''add rows of data_stage01_ale_stocks'''
        if data_I:
            for d in data_I:
                try:
                    data_add = data_stage01_ale_stocks(d
                        #d['experiment_id'],
                        #d['ale_id'],
                        #d['sample_name_abbreviation'],
                        #d['time_point'],
                        #d['ale_time'],
                        #d['ale_time_units'],
                        #d['used_'],
                        #d['comment_']
                        );
                    self.session.add(data_add);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();
    def update_dataStage01AleStocks(self,data_I):
        '''update rows of data_stage01_ale_stocks'''
        if data_I:
            for d in data_I:
                try:
                    data_update = self.session.query(data_stage01_ale_stocks).filter(
                            data_stage01_ale_stocks.id == d['id']).update(
                            {
                            'experiment_id':d['experiment_id'],
                            'ale_id':d['ale_id'],
                            'sample_name_abbreviation':d['sample_name_abbreviation'],
                            'time_point':d['time_point'],
                            'ale_time':d['ale_time'],
                            'ale_time_units':d['ale_time_units'],
                            'used_':d['used_'],
                            'comment_':d['comment_']},
                            synchronize_session=False);
                except SQLAlchemyError as e:
                    print(e);
            self.session.commit();

    def drop_dataStage01_ale_trajectories(self):
        try:
            data_stage01_ale_trajectories.__table__.drop(self.engine,True);
            #data_stage01_ale_jumps.__table__.drop(self.engine,True);
            data_stage01_ale_stocks.__table__.drop(self.engine,True);
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_ale_all(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_ale_trajectories).filter(data_stage01_ale_trajectories.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                #reset = self.session.query(data_stage01_ale_jumps).filter(data_stage01_ale_jumps.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                reset = self.session.query(data_stage01_ale_stocks).filter(data_stage01_ale_stocks.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_ale_trajectories(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_ale_trajectories).filter(data_stage01_ale_trajectories.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_ale_jumps(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                #reset = self.session.query(data_stage01_ale_jumps).filter(data_stage01_ale_jumps.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def reset_dataStage01_ale_stocks(self,experiment_id_I = None):
        try:
            if experiment_id_I:
                reset = self.session.query(data_stage01_ale_stocks).filter(data_stage01_ale_stocks.experiment_id.like(experiment_id_I)).delete(synchronize_session=False);
                self.session.commit();
        except SQLAlchemyError as e:
            print(e);
    def initialize_dataStage01_ale_trajectories(self):
        try:
            data_stage01_ale_trajectories.__table__.create(self.engine,True);
            #data_stage01_ale_jumps.__table__.create(self.engine,True);
            data_stage01_ale_stocks.__table__.create(self.engine,True);
        except SQLAlchemyError as e:
            print(e);