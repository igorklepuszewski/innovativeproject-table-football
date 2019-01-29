package nokia.tablefootball.tablefootballandroid

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.util.Log
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_tables.*
import nokia.tablefootball.tablefootballandroid.activity.helpers.FloorListAdapter
import nokia.tablefootball.tablefootballandroid.activity.helpers.FloorListPump
import nokia.tablefootball.tablefootballandroid.dto.TableDTO
import nokia.tablefootball.tablefootballandroid.service.DataAcquirerAPIController
import nokia.tablefootball.tablefootballandroid.service.DataAcquirerServiceImpl
import nokia.tablefootball.tablefootballandroid.utils.JSONTableParser
import nokia.tablefootball.tablefootballandroid.utils.TableDataUtil

class TablesActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tables)

        val serviceImpl = DataAcquirerServiceImpl(this)
        val controller = DataAcquirerAPIController(serviceImpl)

        val url = intent.extras.getString("URL").toString()

        controller.post(url, null) { response ->
            var expandableListDetail = TableDataUtil.toFloorMapAsStrings(JSONTableParser.parseArray(response))
            /// TODO edit floor list adapter!
            var expandableListTitle = expandableListDetail.keys.toList()
            var expandableListAdapter = FloorListAdapter(
                applicationContext,
                expandableListTitle,
                expandableListDetail
            )
            expandableListView.setAdapter(expandableListAdapter)
        }



//        expandableListView.setOnGroupExpandListener {
//            Toast.makeText(
//                applicationContext,
//                "testX" + " List Expanded.",
//                Toast.LENGTH_SHORT
//            ).show();

        }

    }


/* POC


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_tables)


        var expandableListDetail: HashMap<String, List<String>> = FloorListPump.data
        var expandableListTitle = ArrayList<String>(expandableListDetail.keys)
        var expandableListAdapter = FloorListAdapter(
            this,
            expandableListTitle,
            expandableListDetail
        )
        expandableListView.setAdapter(expandableListAdapter);
        expandableListView.setOnGroupExpandListener {
            Toast.makeText(
                applicationContext,
                "testX" + " List Expanded.",
                Toast.LENGTH_SHORT
            ).show();


        }

        expandableListView.setOnGroupCollapseListener {
            Toast.makeText(
                applicationContext,
                "testX" + " List collapsed.",
                Toast.LENGTH_SHORT
            ).show();

        }

    }



 */