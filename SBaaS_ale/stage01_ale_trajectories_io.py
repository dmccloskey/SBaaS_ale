# System
import json
# SBaaS
from .stage01_ale_trajectories_query import stage01_ale_trajectories_query
from .stage01_ale_analysis_query import stage01_ale_analysis_query

from SBaaS_base.sbaas_template_io import sbaas_template_io
# Resources
from io_utilities.base_importData import base_importData
from io_utilities.base_exportData import base_exportData
from scipy.io import loadmat
from python_statistics.calculate_smoothingFunctions import calculate_smoothingFunctions
from ddt_python.ddt_container import ddt_container

class stage01_ale_trajectories_io(stage01_ale_trajectories_query,
                                  stage01_ale_analysis_query,
                                  sbaas_template_io):

    def import_dataStage01AleTrajectories_matlab(self, experiment_id_I, filename_I):
        '''table adds'''
        #data = base_importData();
        #data.read_csv(filename);
        #data.format_data();
        # load matlab data
        ale_ids = loadmat(filename_I)['ALEsKOs']['ale_id'][0];
        time = loadmat(filename_I)['ALEsKOs']['time'][0];
        growth_rate = loadmat(filename_I)['ALEsKOs']['growth_rate'][0];
        generations = loadmat(filename_I)['ALEsKOs']['generations'][0];
        ccd = loadmat(filename_I)['ALEsKOs']['ccd'][0];
        # format data
        data = [];
        for i,id in enumerate(ale_ids):
            times = [j for j in time[i][0]];
            rates = [j for j in growth_rate[i][0]];
            gens = [j for j in generations[i][0]];
            ccds = [j for j in ccd[i][0]];
            for j,t in enumerate(times):
                data.append({'experiment_id':experiment_id_I,
                                            'ale_id':id[0],
                                            'ale_time':t,
                                            'ale_time_units':'days',
                                            'generations':gens[j],
                                            'ccd':ccds[j],
                                            'rate':rates[j],
                                            'rate_units':'hr-1',
                                            'used_':True,
                                            'comment_':None})
        # add data to table
        self.add_dataStage01AleTrajectories(data);
        #self.add_dataStage01AleTrajectories(data.data);
        #data.clear_data();

    def import_dataStage01AleTrajectories_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01AleTrajectories(data.data);
        data.clear_data();
            
    def import_dataStage01AleJumps_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01AleJumps(data.data);
        data.clear_data();

    def import_dataStage01AleJumps_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01AleJumps(data.data);
        data.clear_data();
            
    def import_dataStage01AleStocks_add(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.add_dataStage01AleStocks(data.data);
        data.clear_data();

    def import_dataStage01AleStocks_update(self, filename):
        '''table adds'''
        data = base_importData();
        data.read_csv(filename);
        data.format_data();
        self.update_dataStage01AleStocks(data.data);
        data.clear_data();

    def export_dataStage01AleTrajectories_js(self,analysis_id_I,fit_func_I='lowess',data_dir_I="tmp"):
        """export data_stage01_ale_trajectories for visualization"""

        print("exporting data_stage01_ale_trajectories...")

        calc = calculate_smoothingFunctions();

        # query the analysis info
        experiment_ids,ale_ids = [],[];
        experiment_ids,ale_ids = self.get_experimentIDAndALEID_analysisID_dataStage01ResequencingAnalysis(analysis_id_I);
        # collect the data and calculate the fitted trajectories
        data_O = []; 
        data1_O={};
        data2_O={};
        data1_O['ale_time'] = [];
        data1_O['generations'] = [];
        data1_O['ccd'] = [];
        data2_O['ale_time'] = [];
        data2_O['generations'] = [];
        data2_O['ccd'] = [];
        for sna_cnt,sna in enumerate(ale_ids):
            #query growth rates and times
            growth_rates = [];
            growth_rates = self.get_rows_experimentIDAndALEID_dataStage01AleTrajectories(experiment_ids[sna_cnt],sna)
            ale_time_units = growth_rates[0]['ale_time_units'];
            rate_units = growth_rates[0]['rate_units'];
            # parse out the data for each ale_id
            x,x_g,x_ccd,y=[],[],[],[];
            for k in growth_rates:
                x.append(k['ale_time'])
                x_g.append(k['generations'])
                x_ccd.append(k['ccd'])
                y.append(k['rate'])
                data1_O['ale_time'].append({'ale_id':sna,
                               'ale_time':k['ale_time'],
                               'ale_time_units':ale_time_units,
                               'rate':k['rate'],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':k['comment_']});
                data1_O['generations'].append({'ale_id':sna,
                               'generations':k['generations'],
                               'rate':k['rate'],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':k['comment_']});
                data1_O['ccd'].append({'ale_id':sna,
                               'ccd':k['ccd'],
                               'rate':k['rate'],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':k['comment_']});
                data_O.append({'ale_id':sna,
                               'ale_time':k['ale_time'],
                               'ale_time_units':ale_time_units,
                               'generations':k['generations'],
                               'ccd':k['ccd'],
                               'rate':k['rate'],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':k['comment_']});
            # generate the fitted data for ale_time
            x_fit,y_fit=[],[];
            x_fit,y_fit=calc.fit_trajectories(x,y,fit_func_I,plot_fit_I=False);
            # restructure into input for d3
            for i,x in enumerate(x_fit):
                data2_O['ale_time'].append({'ale_id':sna,
                               'ale_time':x_fit[i],
                               'ale_time_units':ale_time_units,
                               'rate':y_fit[i],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':None});
            # generate the fitted data for generations
            x_g_fit,y_g_fit=[],[];
            x_g_fit,y_g_fit=calc.fit_trajectories(x_g,y,fit_func_I,plot_fit_I=False);
            # restructure into input for d3
            for i,x in enumerate(x_g_fit):
                data2_O['generations'].append({'ale_id':sna,
                               'generations':x_g_fit[i],
                               'rate':y_g_fit[i],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':None});
            # generate the fitted data for ccd
            x_ccd_fit,y_ccd_fit=[],[];
            x_ccd_fit,y_ccd_fit=calc.fit_trajectories(x_ccd,y,fit_func_I,plot_fit_I=False);
            # restructure into input for d3
            for i,x in enumerate(x_ccd_fit):
                data2_O['ccd'].append({'ale_id':sna,
                               'ccd':x_ccd_fit[i],
                               'rate':y_ccd_fit[i],
                               'rate_units':rate_units,
                               'used_':True,
                               'comment_':None});

        #initialize ddt objects
        dataobject_O = [];
        parametersobject_O = [];
        tile2datamap_O = {};
        filtermenuobject_O=None;
        # make the tile parameter objects
        # tile 1: form
        formtileparameters_O = {
            'tileheader':'Filter menu',
            'tiletype':'html',
            'tileid':"filtermenu1",
            'rowid':"row1",
            'colid':"col1",
            'tileclass':"panel panel-default",
            'rowclass':"row",
            'colclass':"col-sm-4"};
        formparameters_O = {
            "htmltype":'form_01',
            "formsubmitbuttonidtext":{'id':'submit1','text':'submit'},
            "formresetbuttonidtext":{'id':'reset1','text':'reset'},
            "formupdatebuttonidtext":{'id':'update1','text':'update'}};
        formtileparameters_O.update(formparameters_O);
        parametersobject_O.append(formtileparameters_O)
        data1_keys = ['ale_id'];
        data1_nestkeys = ['ale_id'];
        data1_keymap = {'xdata':'ale_time','ydata':'rate','serieslabel':'ale_id','featureslabel':''};
        dataobject_O.append({"data":data_O,"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
        tile2datamap_O.update({"filtermenu1":[0]});
        
        # tile 2-4: trajectors for ale_time, generations, and CCDs
        cnt = 1;
        data_cnt = 1;
        for k in data1_O.keys():
            tileid = "tile"+str(cnt);
            svgid = "svg"+str(cnt);
            colid = "col"+str(cnt+1);
            if k=='ale_time':
                svgx1axislabel = "time (days)";
            else:
                svgx1axislabel = k;
            data1_keys = ['ale_id'];
            data1_nestkeys = ['ale_id'];
            data1_keymap = {
                'xdata':k,
                'ydata':'rate',
                'serieslabel':'ale_id',
                'featureslabel':''};
            dataobject_O.append({"data":data1_O[k],"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
            dataobject_O.append({"data":data2_O[k],"datakeys":data1_keys,"datanestkeys":data1_nestkeys});
            svgparameters_O = {
                "svgtype":'scatterlineplot2d_01',
                "svgkeymap":[data1_keymap,data1_keymap],
                'svgid':svgid,
                "svgmargin":{ 'top': 50, 'right': 150, 'bottom': 50, 'left': 50 },
                "svgwidth":500,"svgheight":350,
                "svgx1axislabel":svgx1axislabel,
                "svgy1axislabel":"growth rate (hr-1)",
                };
            svgtileparameters_O = {
                'tileheader':'ALE trajectories',
                'tiletype':'svg',
                'tileid':tileid,
                'rowid':"row1",
                'colid':colid,
                'tileclass':"panel panel-default",
                'rowclass':"row",
                'colclass':"col-sm-8"};
            svgtileparameters_O.update(svgparameters_O);
            parametersobject_O.append(svgtileparameters_O);
            tile2datamap_O.update({tileid:[data_cnt,data_cnt+1]});
            data_cnt+=2;
            cnt+=1;

        ddtutilities = ddt_container(parameters_I = parametersobject_O,data_I = dataobject_O,tile2datamap_I = tile2datamap_O,filtermenu_I = filtermenuobject_O);
        if data_dir_I=='tmp':
            filename_str = self.settings['visualization_data'] + '/tmp/ddt_data.js'
        elif data_dir_I=='data_json':
            data_json_O = ddtutilities.get_allObjects_js();
            return data_json_O;
        with open(filename_str,'w') as file:
            file.write(ddtutilities.get_allObjects());
   