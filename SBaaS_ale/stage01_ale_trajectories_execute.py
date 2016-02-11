
from .stage01_ale_trajectories_io import stage01_ale_trajectories_io

class stage01_ale_trajectories_execute(stage01_ale_trajectories_io):
    #analyses:
    def execute_findJumps(self,experiment_id_I,sample_name_abbreviations_I=[],fit_func_I='lowess'):
        '''Find jumps in ALE after smoothing trajectories
        TODO: make jump_finder algorithm'''

        #query sample_name abbreviations
        if sample_name_abbreviations_I:
            sample_name_abbreviations = sample_name_abbreviations_I;
        else:
            sample_name_abbreviations = [];
            sample_name_abbreviations = self.get_sampleNameAbbreviations_experimentID_dataStage01AleTrajectories(experiment_id_I);
        for sna in sample_name_abbreviations:
            #query growth rates and times
            growth_rates = [];
            growth_rates = self.get_rows_experimentIDAndSampleNameAbbreviation_dataStage01AleTrajectories(experiment_id_I,sna)
            #smooth growth rates
            x,y=[],[];
            for k in growth_rates:
                x.append(k['ale_time'])
                y.append(k['rate'])
            x_fit,y_fit=[],[];
            x_fit,y_fit=self.calculate.fit_trajectories(x,y,fit_func_I);
            #identify jumps
            jump_start,jump_stop=[],[];
            #jump_start,jump_stop=self.find_jumps(x_fit,y_fit);
            for i,start in enumerate(jump_starts):
                #add rows to the data base
                row = [];
                row = data_stage01_ale_jumps(experiment_id_I, sna,
                        #TODO: jump_start[i],jump_stop[i],
                        True, None);
                self.session.add(row);
        self.session.commit();

    