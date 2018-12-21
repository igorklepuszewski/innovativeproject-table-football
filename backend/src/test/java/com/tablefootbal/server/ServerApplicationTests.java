package com.tablefootbal.server;

import com.tablefootbal.server.dsp.DspAlgorithmsTests;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import org.springframework.boot.test.context.SpringBootTest;

@RunWith(Suite.class)
@SpringBootTest
@Suite.SuiteClasses({SensorRepositoryIntegrationTests.class, SensorDataManagerIntegrationTests.class,
		SensorReadingsTests.class, DspAlgorithmsTests.class})
public class ServerApplicationTests
{
	
	@Test
	public void contextLoads()
	{
	}
	
}
